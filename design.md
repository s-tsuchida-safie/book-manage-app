# 仕様
- ユーザーは本を借りることができる
- 借りられる本の冊数は普段は3冊だがキャンペーン期間中は10冊になる
- 貸出可能な本の在庫がない場合は本を借りることができない
- ユーザーは返却期限までに本を返却する必要がある。返却期限を過ぎた場合は通知がとぶ
- ユーザーは自身を登録することができる
- ユーザーは自身の登録を解除することができる
- ユーザーはメールアドレスの設定を変更することができる
- ユーザーは現在の自身の貸し出し状況を確認することができる
- ユーザーは本のタイトル、ジャンルで検索することができる
- 管理者は本を入荷した場合は本を登録することができる
- 管理者は本の状態が悪い場合は書庫から登録を解除することができる
- 貸出中の場合は本の登録を解除することはできない

# ER図
```mermaid
erDiagram
    User ||--o{ Loan : ""
    User {
        int id PK "ユーザーID"
        string name "ユーザー名"
        string mail_address "メールアドレス"
        datetime created_at "登録日"   
    }
    
    Loan {
        int loan_id PK "貸出ID"
        int user_id FK "ユーザーID"
        int book_id "書籍ID"
        datetime borrowed_at "貸出日"
        datetime returned_at "返却日"
        datetime due_date "返却期限"
    }
    
    %% 別DBのテーブル（参照用として薄く定義）    
    Book {
        int book_id PK "書籍ID"
        string isbn "ISBN"
        string title "書籍のタイトル"
        string description "書籍の紹介文"
        string category "本のジャンル"
        string condition "書籍の状態(NEW / GOOD / BAD / DISCARDED など)"            
    }
```

# システム構成

```mermaid
flowchart LR
    Client["クライアント (Web/App)"]

    subgraph UserLoanService ["User Loan Service (貸出・ユーザー管理)"]
        UserAPI["ユーザー API"]
        LoanAPI["貸出 API"]
        LoanBatch["貸出定期バッチ - 返却期限チェックと通知"]
        UserLoanDB[("User Loan DB")]

        UserAPI --- UserLoanDB
        LoanAPI --- UserLoanDB
        LoanBatch --- UserLoanDB
    end

    subgraph BookService ["Book Service (書籍管理)"]
        BookAPI["書籍 API"]
        BookDB[("Book DB")]
        BookAPI --- BookDB
    end

    Client -->|貸出| LoanAPI
    Client -->|ユーザー登録・解除| UserAPI
    Client -->|書籍検索・閲覧| BookAPI

    LoanAPI -.->|book_id 存在確認とコンディション確認| BookAPI
```