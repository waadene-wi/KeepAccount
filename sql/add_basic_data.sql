-- 【說明】
-- 這個腳本適用的數據庫軟件為：MySQL


-- 添加默認收入分類
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "SALORY", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "BONUS", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "AWARD", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "INVESTMENT", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "LOTTERY", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "UNEXPECTED", 1);
INSERT INTO income_cat1 (cat1_id, nameme, showable) VALUES(NULL, "OTHERS", 1);

-- 添加默認支出一級分類
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "CLOTHES", 1);           -- 2
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "FOOD & DRINK", 1);      -- 3
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "LIVE & LIFE", 1);       -- 4
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "TRANSPORTATION", 1);    -- 5
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "COMMUNICATION", 1);     -- 6
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "ENTERTAINMENT", 1);     -- 7
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "EDUCATION", 1);         -- 8
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "MEDICAL", 1);           -- 9
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "SPORTS", 1);            -- 10
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "INVESTEGATE", 1);       -- 11
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "OTHERS", 1);            -- 12
INSERT INTO payment_cat1 (cat1_id, nameme, showable) VALUES(NULL, "SOCIALITY & GIFT", 1);  -- 13

-- 添加默認支出二級分類
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 2, "CLOTHES", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 2, "SHOES", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 2, "UNDERWARE & SOCKS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 2, "DECORATION", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 2, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "3MEALS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "SNAKES", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "DRINKS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "FRUITS & NUTS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "FOOD INGREDIENT", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 3, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "HOUSE RENTAL", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "W & E & G", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "WARM & PROTERTY", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "FURNITURE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "ELECTRICAL", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "TOOLS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "DAILY EXPENDITURE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "HAIRDRESSING & BEAUTY", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "TEXTILE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 4, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "PUBLIC TRANS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "TAXI", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "RENT CAR", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "PETROL", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "PUBLIC BIKE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "TRAIN & PLANE & SHIP", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 5, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 6, "MOBILE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 6, "NETWORK", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 6, "MAIL", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 6, "OTHER", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "NOVEL & COMICS & MAGZINE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "ELECTRONIC DEVICE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "CD & DVD", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "TOYS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "GAMES", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "MOVIE & SHOW", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "ENTERTAINMENT PLACE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 7, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 8, "BOOKS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 8, "STATIONERY", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 8, "STUDY FEE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 8, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 9, "MEDICAL", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 9, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 10, "SPORTS EQUIPMENT", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 10, "PLACE FEE", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 10, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 11, "LOTTERY", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 11, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 12, "REMEDY RECORD", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 12, "LOST", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 12, "OTHERS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 13, "MONEY FOR RELATIVES", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 13, "MONEY FOR FRIENDS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 13, "GIFTS", 1);
INSERT INTO payment_cat2 (cat2_id, cat1_id, nameme, showable) VALUES(NULL, 13, "OTHERS", 1);

-- 添加默認轉賬分類
INSERT INTO transfer_cat1 (cat1_id, nameme, showable) VALUES(NULL, "BORROW IN", 1);
INSERT INTO transfer_cat1 (cat1_id, nameme, showable) VALUES(NULL, "RETURN BACK", 1);
INSERT INTO transfer_cat1 (cat1_id, nameme, showable) VALUES(NULL, "LEND OUT", 1);
INSERT INTO transfer_cat1 (cat1_id, nameme, showable) VALUES(NULL, "RETURN IN", 1);
INSERT INTO transfer_cat1 (cat1_id, nameme, showable) VALUES(NULL, "OTHER", 1);

-- 添加默認幣種
INSERT INTO currency (crc_id, nameme, unit, characterter, showable) VALUES(1, "CNY", "Yuan", "¥", 1);
INSERT INTO currency (crc_id, nameme, unit, characterter, showable) VALUES(2, "USD", "Dollar", "$", 1);
INSERT INTO currency (crc_id, nameme, unit, characterter, showable) VALUES(3, "JPY", "Yen", "￥", 1);
INSERT INTO currency (crc_id, nameme, unit, characterter, showable) VALUES(4, "HKD", "Yen", "HK$", 1);

-- 添加常用賬戶
INSERT INTO account VALUES(NULL, 1, 1, "CNY_Financing", 1, 0);

