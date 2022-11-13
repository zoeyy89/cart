/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 物品庫存資料表
DROP TABLE IF EXISTS `in_stock_products` ;

CREATE TABLE `in_stock_products` (
  `product_id`  int(10) unsigned NOT NULL AUTO_INCREMENT,   -- 物品編號 (PRIMARY KEY)
  `name`        varchar(25) DEFAULT NULL,                   -- 物品名稱
  `price`       int(10) DEFAULT NULL,                       -- 單價
  `quantity`    int(10) unsigned DEFAULT NULL,              -- 庫存量
  `created_at`  timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`  timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;

-- ============================
-- 購物車 資料表 (一人只能有一個購物車)
DROP TABLE IF EXISTS `user_carts` ;

CREATE TABLE `user_carts` (
  `user_id`    varchar(8) DEFAULT NULL,                    -- user id  (PRIMARY KEY)
  `name`       varchar(25) DEFAULT NULL,                   -- 客戶名稱
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at` timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;

-- ============================
-- 購物車內物品 資料表
-- 購物車轉訂單必須將此人的購物車清空
DROP TABLE IF EXISTS `cart_products` ;

CREATE TABLE `cart_products` (
  `cart_products_id` int(10) unsigned NOT NULL AUTO_INCREMENT,   -- 購物車內物品 ID (PRIMARY KEY)
  `user_id`          varchar(8) NOT NULL DEFAULT '0',            -- user id
  `product_id`       int(10) unsigned NOT NULL DEFAULT '0',      -- 物品編號
  `name`             varchar(25) DEFAULT NULL,                   -- 物品名稱
  `price`            int(10) DEFAULT NULL,                       -- 單價  
  `quantity`         int(10) unsigned DEFAULT NULL,              -- 數量
  `created_at`       timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`       timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`cart_products_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;

-- ============================
-- 訂單 資料表
DROP TABLE IF EXISTS `orders` ;

CREATE TABLE `orders` (
  `order_id`          int(10) unsigned NOT NULL AUTO_INCREMENT,   -- 訂單 ID (PRIMARY KEY)
  `user_id`           varchar(8) DEFAULT NULL,                    -- user id
  `total_price`       int unsigned DEFAULT NULL,                  -- 訂單金額
  `shipped`           char(1) DEFAULT 'N',                        -- 已出貨 
  `shipped_datetime`  char(1) DEFAULT NULL,                       -- 出貨日期時間
  `created_at`        timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`        timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;


-- ============================
-- 訂單內物品 資料表
DROP TABLE IF EXISTS `order_products`;

CREATE TABLE `order_products` (
  `order_product_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id`         int(10) unsigned NOT NULL DEFAULT '0',
  `product_id`       int(10) unsigned NOT NULL DEFAULT '0',      -- 物品編號
  `name`             varchar(25) DEFAULT NULL,                   -- 物品名稱
  `price`            int(10) DEFAULT NULL,                       -- 單價  
  `quantity`         int(10) unsigned DEFAULT NULL,              -- 數量
  `created_at`       timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`       timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`order_product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;


-- ============================
-- 入庫單 資料表
DROP TABLE IF EXISTS `stock_in_forms` ;

CREATE TABLE `stock_in_forms` (
  `stock_in_form_id` int(10) unsigned NOT NULL AUTO_INCREMENT,   -- 入庫單 ID (PRIMARY KEY)
  `created_at`       timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`       timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`stock_in_form_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;


-- ============================
-- 入庫單物品 資料表
DROP TABLE IF EXISTS `stock_in_forms_products` ;

CREATE TABLE `stock_in_forms_products` (
  `stock_in_forms_product_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `stock_in_form_id`          int(10) unsigned NOT NULL DEFAULT '0',
  `product_id`                int(10) unsigned NOT NULL DEFAULT '0',      -- 物品編號
  `name`                      varchar(250) DEFAULT NULL,                  -- 物品名稱  
  `quantity`                  int(10) unsigned DEFAULT NULL,              -- 數量
  `created_at`                timestamp DEFAULT CURRENT_TIMESTAMP,        -- 建檔時間
  `updated_at`                timestamp NULL ON UPDATE CURRENT_TIMESTAMP, -- 資料最後異動時間
  PRIMARY KEY (`stock_in_forms_product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ;


