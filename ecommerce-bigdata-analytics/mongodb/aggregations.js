/*Product Popularity*/
db.transactions.aggregate([
 {$unwind:"$items"},
 {$group:{
   _id:"$items.product_id",
   total_quantity:{$sum:"$items.quantity"},
   revenue:{$sum:"$items.subtotal"}
 }},
 {$sort:{total_quantity:-1}},
 {$limit:10}
])

/*Revenue by Category*/
db.transactions.aggregate([
 {$unwind:"$items"},
 {$lookup:{
   from:"products",
   localField:"items.product_id",
   foreignField:"_id",
   as:"product"
 }},
 {$unwind:"$product"},
 {$group:{
   _id:"$product.category.category_name",
   revenue:{$sum:"$items.subtotal"}
 }},
 {$sort:{revenue:-1}}
])