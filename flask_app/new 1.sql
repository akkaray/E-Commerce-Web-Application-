
create procedure ETLRevenueFactAppend()
begin




CREATE TABLE intermediateRevenueFactTable as
SELECT sv.noofitems, sv.noofitems*p.productprice as RevenueGenerated, st.customerid, st.storeid, sv.productid, st.tdate, st.t_id, 'Sales' AS RevenueType
FROM goelr_Zagimore_retail.product p, goelr_Zagimore_retail.soldvia sv, goelr_Zagimore_retail.salestransaction st
WHERE p.productid = sv.productid
AND sv.t_id = st.t_id
AND st.tdate > (SELECT DATE((SELECT MAX(f_timestamp) FROM goelr_ZAGI_DATASTAGING.Core_Revenue)));

ALTER TABLE `intermediateRevenueFactTable` CHANGE `RevenueType` `RevenueType` VARCHAR( 15 );

INSERT INTO intermediateRevenueFactTable(noofitems,customerid, tdate, storeid,productid, RevenueGenerated, t_id, RevenueType)
SELECT '1', c.customerid, st.tdate, s.storeid, p.productid, p.productpricedaily * sv.duration, st.t_id, 'Rentals,Daily'
FROM goelr_Zagimore_retail.rentalProducts p, goelr_Zagimore_retail.rentvia sv, goelr_Zagimore_retail.rentaltransaction st, 
goelr_Zagimore_retail.customer c, goelr_Zagimore_retail.store s
WHERE p.productid = sv.productid
AND sv.t_id = st.t_id
AND st.customerid = c.customerid
AND st.storeid=s.storeid
AND sv.rentaltype='D'
AND st.tdate > (SELECT DATE((SELECT MAX(f_timestamp) FROM goelr_ZAGI_DATASTAGING.Core_Revenue)));

INSERT INTO intermediateRevenueFactTable (noofitems,customerid, tdate, storeid,productid, RevenueGenerated, t_id, RevenueType)
SELECT '1', c.customerid, st.tdate, s.storeid, p.productid, p.productpricedaily * sv.duration, st.t_id, 'Rentals,Weekly'
FROM goelr_Zagimore_retail.rentalProducts p, goelr_Zagimore_retail.rentvia sv, goelr_Zagimore_retail.rentaltransaction st, goelr_Zagimore_retail.customer c, goelr_Zagimore_retail.store s
WHERE p.productid = sv.productid
AND sv.t_id = st.t_id
AND st.customerid = c.customerid
AND st.storeid=s.storeid
AND sv.rentaltype='W'
AND st.tdate > (SELECT DATE((SELECT MAX(f_timestamp) FROM goelr_ZAGI_DATASTAGING.Core_Revenue)));

INSERT INTO Core_Revenue(CustomerKey, ProductKey, StoreKey, UnitsSold, RevenueGenerated, CalendarKey, t_id, f_timestamp, loaded, RevenueType)
SELECT c.CustomerKey, p.ProductKey, s.StoreKey, i.noofitems,
i.RevenueGenerated, ca.CalendarKey, i.t_id, NOW(), FALSE, RevenueType
FROM intermediateRevenueFactTable i, CustomerDimension c,
StoreDimension s, ProductDimension p, CalendarDimension ca
WHERE i.customerid = c.customerid
AND i.storeid = s.storeid
AND i.productid = p.productid

AND LEFT(i.RevenueType,1) = LEFT(p.ProductType, 1)
AND i.tdate = ca.fulldate;


INSERT INTO goelr_ZagiDataWarehouse.Core_Revenue(CustomerKey, ProductKey, StoreKey, UnitsSold, RevenueGenerated, CalendarKey, t_id, RevenueType)
SELECT CustomerKey, ProductKey, StoreKey, UnitsSold, RevenueGenerated, CalendarKey, t_id, RevenueType
FROM Core_Revenue
WHERE loaded = 0;

UPDATE Core_Revenue
SET loaded = 1;
end




SELECT * FROM demo_addresses
LEFT JOIN demo_users ON demo_users.id = demo_addresses.uid