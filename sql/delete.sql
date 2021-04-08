USE keepaccount;

DELETE FROM account;
DELETE FROM account_balance;
DELETE FROM annually_stat_record;
DELETE FROM budget_plan WHERE cat1_id != 1;
DELETE FROM currency;
DELETE FROM daily_stat_record;
DELETE FROM income_cat1;
DELETE FROM income_record;
DELETE FROM monthly_stat_record;
DELETE FROM payment_cat1 WHERE cat1_id != 1;
DELETE FROM payment_cat2;
DELETE FROM payment_record;
DELETE FROM transfer_cat1;
DELETE FROM transfer_record;
