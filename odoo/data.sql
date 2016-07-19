select	'PO',left(poc_date,6) , 
		count(*)
		from 
trade.t_t_mPOC_master
where left(poc_date,4)>='2015' 
group by left(poc_date,6)
union all 
select	'SO',left(ord_date,6) , 
		count(*)
		from 
trade.t_t_sOrder_master
where left(ord_date,4)>='2015' 
group by left(ord_date,6)