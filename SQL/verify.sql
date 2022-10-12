\echo "Checking row in dim_customer Table"
select count(*) from "dim_customer";

\echo "Checking row in dim_city Table"
select count(*) from "dim_city";

\echo "Checking row in dim_product Table"
select count(*) from "dim_product";

\echo "Checking row in fact_sales Table"
select count(*) from "fact_sales";
