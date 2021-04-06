
-- 【說明】
-- 這個腳本適用的數據庫軟件為：SQLite
-- 金額相關的字段單位為1/100標準單位。例如，幣種為人民幣時，單位為分，為美元時，單位為美分。
-- 時間相關的字段單位為秒



CREATE TABLE INCOME_CAT1(
    CAT1_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAMEME VARCHAR(32) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE PAYMENT_CAT1(
    CAT1_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAMEME VARCHAR(32) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

INSERT INTO PAYMENT_CAT1 VALUES(1, 'PLACEHOLDERFORALLPAYMENTCAT1', 0);

CREATE TABLE TRANSFER_CAT1(
    CAT1_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAMEME VARCHAR(32) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE PAYMENT_CAT2(
    CAT2_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CAT1_ID INTEGER NOT NULL,
    NAMEME VARCHAR(32) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE CURRENCY (
    CRC_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAMEME VARCHAR(32) NOT NULL,
    UNIT VARCHAR(32) NOT NULL,
    CHARACTERTER VARCHAR(8) NOT NULL
);

CREATE TABLE ACCOUNT (
    ACNT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CRC_ID INTEGER NOT NULL,
    NAMEME VARCHAR(32) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE ACCOUNT_BALANCE (
    ACNT_ID INTEGER PRIMARY KEY,
    BALANCECE BIGINT NOT NULL
);

CREATE TABLE INCOME_RECORD (
    RCD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ACNT_ID INTEGER NOT NULL, -- 1:CASH 2:DEBET 3:REDEBET
    TIMEME BIGINT NOT NULL,
    AMOUNT BIGINT NOT NULL,
    CAT1_ID INTEGER NOT NULL,
    DESCRIBEBE VARCHAR(72) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE PAYMENT_RECORD (
    RCD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ACNT_ID INTEGER NOT NULL, -- 1:CASH 2:DEBET 3:REDEBET
    TIMEME BIGINT NOT NULL,
    AMOUNT BIGINT NOT NULL,
    CAT1_ID INTEGER NOT NULL,
    CAT2_ID INTEGER NOT NULL,
    DESCRIBEBE VARCHAR(72) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE TRANSFER_RECORD (
    RCD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIMEME BIGINT NOT NULL,
    AMOUNT BIGINT NOT NULL,
    CAT1_ID INTEGER NOT NULL,
    SRC_ACNT_ID INTEGER NOT NULL,
    DST_ACNT_ID INTEGER NOT NULL,
    DESCRIBEBE VARCHAR(72) NOT NULL,
    SHOWABLE TINYINT NOT NULL
);

CREATE TABLE DAILY_STAT_RECORD (
    TIMEME BIGINT NOT NULL,
    INCOME BIGINT NOT NULL,
    PAYMENT BIGINT NOT NULL,
    PRIMARY KEY(TIMEME)
);

CREATE TABLE MONTHLY_STAT_RECORD (
    TIMEME BIGINT NOT NULL,
    INCOME BIGINT NOT NULL,
    PAYMENT BIGINT NOT NULL,
    PRIMARY KEY(TIMEME)
);

CREATE TABLE ANNUALLY_STAT_RECORD (
    TIMEME BIGINT NOT NULL,
    INCOME BIGINT NOT NULL,
    PAYMENT BIGINT NOT NULL,
    PRIMARY KEY(TIMEME)
);

-- 每個一級支出分類都必須有一條預算記錄，默認值為全零
CREATE TABLE BUDGET_PLAN (
    PAYMENT_CAT1_ID INTEGER NOT NULL,
    MON1 BIGINT NOT NULL,
    MON2 BIGINT NOT NULL,
    MON3 BIGINT NOT NULL,
    MON4 BIGINT NOT NULL,
    MON5 BIGINT NOT NULL,
    MON6 BIGINT NOT NULL,
    MON7 BIGINT NOT NULL,
    MON8 BIGINT NOT NULL,
    MON9 BIGINT NOT NULL,
    MON10 BIGINT NOT NULL,
    MON11 BIGINT NOT NULL,
    MON12 BIGINT NOT NULL,
    ALL_YEAR BIGINT NOT NULL,
    PRIMARY KEY(PAYMENT_CAT1_ID),
    FOREIGN KEY(PAYMENT_CAT1_ID) REFERENCES PAYMENT_CAT1(CAT1_ID)
);

INSERT INTO BUDGET_PLAN VALUES(1,0,0,0,0,0,0,0,0,0,0,0,0,0); -- 第一行記錄作為全年所有分類總預算

