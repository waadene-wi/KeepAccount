
-- 【說明】
-- 這個腳本適用的數據庫軟件為：SQLite
-- 金額相關的字段單位為1/100標準單位。例如，幣種為人民幣時，單位為分，為美元時，單位為美分。
-- 時間相關的字段單位為秒



CREATE TABLE income_cat1(
    cat1_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameme VARCHAR(32) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE payment_cat1(
    cat1_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameme VARCHAR(32) NOT NULL,
    showable TINYINT NOT NULL
);

INSERT INTO payment_cat1 VALUES(1, 'PLACEHOLDERFORALLPAYMENTCAT1', 0);

CREATE TABLE transfer_cat1(
    cat1_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameme VARCHAR(32) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE payment_cat2(
    cat2_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat1_id INTEGER NOT NULL,
    nameme VARCHAR(32) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE currency (
    crc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameme VARCHAR(32) NOT NULL,
    unit VARCHAR(32) NOT NULL,
    characterter VARCHAR(8) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE account (
    acnt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crc_id INTEGER NOT NULL,
    typepe TINYINT NOT NULL, -- 1:Normal, 2:Debet, 3:Loan
    nameme VARCHAR(32) NOT NULL,
    showable TINYINT NOT NULL,
    deleteable TINYINT NOT NULL
);

CREATE TABLE account_balance (
    acnt_id INTEGER PRIMARY KEY,
    balance BIGINT NOT NULL
);

CREATE TRIGGER add_account AFTER INSERT ON currency
BEGIN
    INSERT INTO account VALUES(NULL, new.crc_id, 1, new.nameme || "_NORMAL", 1, 0);
    INSERT INTO account VALUES(NULL, new.crc_id, 2, new.nameme || "_DEBET", 1, 0);
    INSERT INTO account VALUES(NULL, new.crc_id, 3, new.nameme || "_LOAN", 1, 0);
END;

CREATE TRIGGER add_account_balance AFTER INSERT ON account
BEGIN
    INSERT INTO account_balance VALUES(new.acnt_id, 0);
END;

CREATE TABLE income_record (
    rcd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    acnt_id INTEGER NOT NULL, -- 1:CASH 2:DEBET 3:REDEBET
    timeme BIGINT NOT NULL,
    amount BIGINT NOT NULL,
    cat1_id INTEGER NOT NULL,
    describebe VARCHAR(72) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE payment_record (
    rcd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    acnt_id INTEGER NOT NULL, -- 1:CASH 2:DEBET 3:REDEBET
    timeme BIGINT NOT NULL,
    amount BIGINT NOT NULL,
    cat1_id INTEGER NOT NULL,
    cat2_id INTEGER NOT NULL,
    describebe VARCHAR(72) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE transfer_record (
    rcd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timeme BIGINT NOT NULL,
    amount BIGINT NOT NULL,
    cat1_id INTEGER NOT NULL,
    SRC_acnt_id INTEGER NOT NULL,
    DST_acnt_id INTEGER NOT NULL,
    describebe VARCHAR(72) NOT NULL,
    showable TINYINT NOT NULL
);

CREATE TABLE daily_stat_record (
    timeme BIGINT NOT NULL,
    crc_id INTEGER NOT NULL,
    income BIGINT NOT NULL,
    payment BIGINT NOT NULL,
    PRIMARY KEY(timeme, crc_id)
);

CREATE TABLE monthly_stat_record (
    timeme BIGINT NOT NULL,
    crc_id INTEGER NOT NULL,
    income BIGINT NOT NULL,
    payment BIGINT NOT NULL,
    PRIMARY KEY(timeme, crc_id)
);

CREATE TABLE annually_stat_record (
    timeme BIGINT NOT NULL,
    crc_id INTEGER NOT NULL,
    income BIGINT NOT NULL,
    payment BIGINT NOT NULL,
    PRIMARY KEY(timeme, crc_id)
);

-- 每個一級支出分類都必須有一條預算記錄，默認值為全零
CREATE TABLE budget_plan (
    payment_cat1_id INTEGER NOT NULL,
    mon1 BIGINT NOT NULL,
    mon2 BIGINT NOT NULL,
    mon3 BIGINT NOT NULL,
    mon4 BIGINT NOT NULL,
    mon5 BIGINT NOT NULL,
    mon6 BIGINT NOT NULL,
    mon7 BIGINT NOT NULL,
    mon8 BIGINT NOT NULL,
    mon9 BIGINT NOT NULL,
    mon10 BIGINT NOT NULL,
    mon11 BIGINT NOT NULL,
    mon12 BIGINT NOT NULL,
    all_year BIGINT NOT NULL,
    PRIMARY KEY(payment_cat1_id)
);

INSERT INTO budget_plan VALUES(1,0,0,0,0,0,0,0,0,0,0,0,0,0); -- 第一行記錄作為全年所有分類總預算

