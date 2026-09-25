# 仕様
- ユーザーはログインしてトークンを取得・保持する必要がある
- ユーザーは自身を登録することができる
- ユーザーは自身の登録を解除することができる
- ユーザーはメールアドレスの設定を変更することができる
- ユーザーは本のタイトル、ジャンルで検索することができる
- ユーザーは本を借りることができる
- 借りられる本の冊数は普段は3冊だがキャンペーン期間中は10冊になる
- 貸出可能な本の在庫がない場合は本を借りることができない
- ユーザーは返却期限までに本を返却する必要がある。返却期限を過ぎた場合は通知がとぶ
- ユーザーは現在の自身の貸し出し状況を確認することができる
- 管理者はログインしてトークンを取得・保持する必要がある
- 管理者は本を入荷した場合は本を登録することができる
- 管理者は本の状態が悪い場合は書庫から登録を解除することができる
- 貸出中の場合は本の登録を解除することはできない

# ER図
```mermaid
erDiagram
    User {
        int user_id PK "ユーザーID"
        string name "ユーザー名"
        string mail_address "メールアドレス"
        datetime created_at "登録日"
        int role_id "権限(1: 一般ユーザー / 2: 管理者)"
        string password_hash "ハッシュ化パスワード"
        string token "認証トークン"
    }
    
    Loan {
        int loan_id PK "貸出ID"
        int user_id "ユーザーID"
        int book_id "書籍ID"
        datetime borrowed_at "貸出日"
        datetime returned_at "返却日"
        datetime due_date "返却期限"
    }
      
    Book {
        int book_id PK "書籍ID"
        string isbn "ISBN"
        string title "書籍のタイトル"
        string description "書籍の紹介文"
        string category "本のジャンル"
        string condition "書籍の状態(NEW / GOOD / BAD / DISCARDED)"            
    }
```

# システム構成

```mermaid
flowchart LR
    Client["クライアント (Web/App)"]

    subgraph APIGatewayService ["API Gateway Service (FastAPI)"]
        GatewayAPI["Gateway API<br>・リクエストルーティング<br>・JWT共通署名検証<br>・Swagger UIの一括提供"]
    end

    subgraph AuthUserService ["Auth User Service (ユーザー・管理者認証)"]
        AuthAPI["認証 API"]
        AuthUserDB[("Auth User DB")]
        AuthAPI --- AuthUserDB
    end

    subgraph UserLoanService ["User Loan Service (貸出・ユーザー管理)"]
        LoanAPI["貸出 API"]
        LoanBatch["貸出定期バッチ - 返却期限チェックと通知"]
        LoanDB[("Loan DB")]
        LoanAPI --- LoanDB
        LoanBatch --- LoanDB
    end

    subgraph BookService ["Book Service (書籍管理)"]
        BookAPI["書籍 API"]
        BookDB[("Book DB")]
        BookAPI --- BookDB
    end

    %% クライアントは Gateway API だけと通信する
    Client -->|"1. すべてのリクエスト (HTTP/HTTPS)"| GatewayAPI

    %% Gateway から裏側の各マイクロサービスへ中継（httpx等）
    GatewayAPI -->|"/auth/* へ転送"| AuthAPI
    GatewayAPI -->|"/loans/* へ転送"| LoanAPI
    GatewayAPI -->|"/books/* へ転送"| BookAPI

    %% サービス間（内部）の直接通信・検証
    GatewayAPI -.->|JWT 署名検証| AuthAPI
    LoanAPI -.->|book_id 存在確認とコンディション確認| BookAPI
    BookAPI -.->|書籍削除時の貸出中チェック| LoanAPI
```