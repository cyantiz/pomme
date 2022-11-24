interface Image {
    image_id: number
    product_id: number
    is_thumbnail: boolean
    url: string
}

interface Product {
    product_id: number
    name: string
    price: number
    sale_percent: number
    in_stock: number
    images: Image[]
    type: 1 | 2 | 3
    // 1: shoe | 2: accessory | 3: clothes
}

interface Shoe {
    shoe_id: number
    product_id: number
    gender: 0 | 1 | 2
    series: String
    shape: 0 | 1
    product: Product
}

interface ShoeChild {
    shoe_child_id: number
    shoe_id: number
    size: number
    in_stock: number
}

interface Clothes {
    clothes_id: number
    product_id: number
    category: 1 | 2 | 3
    // 1: tee, 2: hoodie, 3:sweatshirt

    product: Product
}

interface Accessory {
    accessory_id: number
    product_id: number
    category: 1 | 2 | 3 | 4
    // 1: shock, 2: tote, 3: backpack, 4: shoelace
    product: Product
}

interface UserCartProduct {
    user_cart_product_id: number
    user_id: number
    product_id: number
    quantity: number
    size: number | null
    product: Product
}

interface OrderProduct {
    order_product_id: number
    order_id: number
    product_id: number
    price_at_order: number
    quantity: number
    product: Product
    size: number | null
}

interface Order {
    order_id: number
    user_id: number
    address: string
    province_id: number
    district_id: number
    commune_id: number
    status: 0 | 1 | 2
    // 0 = in progress, 1 = shipping, 2 = delivered
    total: number
    discount: number
    created_at: string
    shipping_at: string
    delivered_at: string
    products: OrderProduct[]
}
