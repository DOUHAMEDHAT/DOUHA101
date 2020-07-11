-- Main Query of the Tables:
CREATE VIEW ecommerce AS 
SELECT    
	ooid.*,
    ood.customer_id, ood.order_status, ood.order_purchase_timestamp, ood.order_approved_at, ood.order_delivered_carrier_date, ood.order_delivered_customer_date, ood.order_estimated_delivery_date,
    ocd.customer_unique_id, ocd.customer_zip_code_prefix, ocd.customer_city, ocd.customer_state,
    -- oord.review_id, oord.review_score, oord.review_comment_title, oord.review_comment_message, oord.review_creation_date, oord.review_answer_timestamp,
    opd.product_category_name, opd.product_name_lenght, opd.product_description_lenght, opd.product_photos_qty, opd.product_weight_g, opd.product_length_cm, opd.product_height_cm, opd.product_width_cm,
    osd.seller_zip_code_prefix, osd.seller_city, osd.seller_state,
    pcnt.product_category_name_english
                    
FROM items ooid
LEFT JOIN orders ood ON ood.order_id = ooid.order_id
LEFT JOIN customers ocd ON ocd.customer_id = ood.customer_id
-- LEFT JOIN reviews oord ON oord.order_id = ood.order_id
LEFT JOIN payments oopd ON oopd.order_id = ood.order_id
LEFT JOIN products opd ON opd.product_id = ooid.product_id
LEFT JOIN sellers osd ON osd.seller_id = ooid.seller_id
LEFT JOIN category pcnt ON pcnt.product_category_name = opd.product_category_name
;
