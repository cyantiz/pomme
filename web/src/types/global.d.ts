interface Image {
    id: number
    product_id: number
    is_thumbnail: boolean
    url: string
}

interface Product {
    id: number
    name: string
    price: number
    sold: number
    discount_percent: number
    in_stock: number
    type: string
}

interface Shoe {
    id: number
    product_id: number
    gender: 0 | 1 | 2
    series: string
    shape: 0 | 1
}

interface ShoeChild {
    id: number
    shoe_id: number
    size: number
    in_stock: number
}

interface Clothes {
    id: number
    product_id: number
    category: string
}

interface Accessory {
    id: number
    product_id: number
    category: string
}

interface UserCartPivot {
    id: number
    user_id: number
    product_id: number
    quantity: number
    size: number | null
}
interface UserCartProduct extends ProductWithThumbnail {
    pivot: UserCartPivot
}

interface OrderProductPivot {
    order_id: number
    product_id: number
    price_at_order: number
    quantity: number
    size: number | null
}
interface OrderProduct extends ProductWithThumbnail {
    pivot: OrderProductPivot
}

interface Order {
    id: number
    name: string
    user_id: number
    address: string
    province_id: string
    district_id: string
    commune_id: string
    status: string
    phone: string
    total_price: number
    delivery_fee: number
    discount: number
    created_at: string
    shipping_at: string
    delivered_at: string
    image_url: string
}

interface OrderWithProducts extends Order {
    products: OrderProduct[]
}

interface ProductWithImages extends Product {
    images: Image[]
}

interface ProductWithThumbnail extends Product {
    thumbnail: Image
}

interface ShoeWithProduct extends Shoe {
    product: ProductWithImages
}

interface ShoeWithProductAndChild extends ShoeWithProduct {
    children: ShoeChild[]
}

interface AccessoryWithProduct extends Accessory {
    product: ProductWithImages
}

interface ClothesWithProduct extends Clothes {
    product: ProductWithImages
}

interface AuthData {
    access_token: string
    token_type: string
    expires_at: number
    user: User
}

interface User {
    id: number
    email: string
    name: string
    role: string
}

interface LoginForm {
    email: string
    password: string
}

interface CartAddingForm {
    product_id: number
    quantity: number
    size?: number
}
