# 📊 Automated Sales Data Pipeline using Airflow and Docker

## 1. Tổng quan dự án

Dự án này xây dựng một pipeline ETL end-to-end cho dữ liệu giao dịch bán hàng, sử dụng Apache Airflow, PostgreSQL và Docker.

Mục tiêu của dự án là ingest dữ liệu bán hàng thô từ file CSV, thực hiện làm sạch và kiểm tra chất lượng dữ liệu, sau đó lưu trữ dữ liệu vào bảng Data Warehouse sẵn sàng cho việc truy vấn và phân tích.

Dự án được thực hiện như một Final Project môn Data Engineering, tập trung vào:

Orchestration pipeline bằng Airflow

Kiểm soát chất lượng dữ liệu (Data Quality)

Logging và monitoring

Khả năng tái tạo hệ thống bằng Docker

## 2. Vấn đề đặt ra (Problem Statement)

Trong thực tế, dữ liệu giao dịch bán hàng của doanh nghiệp bán lẻ thường được export thủ công từ hệ thống POS dưới dạng file CSV hoặc Excel.

***Những dữ liệu thô này thường gặp các vấn đề:***

Chưa được chuẩn hóa schema

Có khả năng trùng lặp hóa đơn

Không có kiểm tra chất lượng dữ liệu

Khó sử dụng trực tiếp cho phân tích

***Do đó, cần xây dựng một pipeline ETL tự động để:***

Ingest dữ liệu thô

Làm sạch và validate dữ liệu

Lưu trữ dữ liệu có cấu trúc cho phân tích

## 3. Dataset

Tên dataset: Supermarket Sales
File gốc excel download chuyển thành csv

File dữ liệu: Supermarket_sales.csv

Mức độ chi tiết: Transaction-level (theo hóa đơn)

Các trường chính:

- Invoice ID

- Date

- Branch / City

- Product line

- Quantity

- Unit price

- Total

## 4. Kiến trúc Pipeline

Supermarket_sales.csv
        ↓
raw_supermarket_sales
        ↓
clean_supermarket_sales
        ↓
fact_sales

Các layer:

- Raw layer: Lưu dữ liệu đúng như nguồn CSV, không chỉnh sửa

- Clean layer: Áp dụng các rule làm sạch và kiểm tra chất lượng

- Serve layer (Fact table): Sẵn sàng cho truy vấn và phân tích

- Pipeline được thiết kế theo kiến trúc Raw → Clean → Serve, giúp đảm bảo tính rõ ràng, dễ kiểm soát và mở rộng.

## 5. Quy tắc làm sạch & kiểm tra dữ liệu

Các quy tắc sau được áp dụng tại clean layer:

| Quy tắc                       | Mục đích                         |
| ----------------------------- | -------------------------------- |
| Quantity > 0                  | Kiểm tra logic dữ liệu           |
| Unit price > 0                | Kiểm tra logic dữ liệu           |
| Total = Quantity × Unit price | Đảm bảo tính nhất quán           |
| Loại bỏ Invoice ID trùng lặp  | Tránh double counting            |
| Parse cột Date                | Phục vụ phân tích theo thời gian |

## 6. Logging & Data Quality Monitoring

***Pipeline có cơ chế logging và kiểm tra chất lượng dữ liệu như sau:***

- **Logging**

- **Mỗi task trong pipeline (Extract, Clean, Load, Data Quality Check) đều ghi log**

- **Log được lưu trực tiếp trong Airflow Task Logs**

***Thông tin log bao gồm:***

- **Số lượng bản ghi xử lý**

- **Trạng thái thực thi**

- **Kết quả kiểm tra data**

- **Data Quality Check**

***Một task riêng biệt dùng để so sánh số lượng bản ghi giữa:***

Raw layer
Clean layer

Pipeline sẽ fail tự động nếu số lượng bản ghi bị giảm vượt ngưỡng cho phép

Cách tiếp cận này giúp phát hiện sớm các vấn đề mất dữ liệu và đảm bảo độ tin cậy của dữ liệu đầu ra.

## 7. Công nghệ sử dụng

-**Apache Airflow – Orchestration và monitoring pipeline**

-**PostgreSQL – Lưu trữ dữ liệu**

**Docker & Docker Compose – Triển khai hệ thống dạng container**

-**Dockerfile – Custom môi trường Airflow và dependency**

-**Python – Xử lý ETL**

-**Pandas – Xử lý dữ liệu**

-**SQLAlchemy – Kết nối và thao tác với database**

8. Cấu trúc project

sales_etl_project/
├── dags/
│   └── sales_etl_dag.py        # Airflow DAG
├── scripts/
│   ├── extract.py              # Load CSV vào raw layer
│   ├── clean.py                # Clean & validate dữ liệu
│   ├── load.py                 # Load dữ liệu vào fact table
│   ├── quality_check.py        # Data quality check
│   └── db.py                   # Kết nối PostgreSQL
├── data/
│   └── Supermarket_sales.csv
├── Dockerfile                  # Custom Airflow image
├── docker-compose.yml          # Airflow + PostgreSQL
├── requirements.txt            # Python dependencies
└── README.md

## 9. Airflow DAG

- ***Tên DAG:*** sales_etl_pipeline

- ***Schedule:*** Trigger thủ công

***Các task chính:***

Extract dữ liệu từ CSV vào raw layer

Clean & validate dữ liệu

Data quality check

Load dữ liệu vào fact table

Pipeline được trigger và theo dõi thông qua Airflow Web UI.

## 10. Hướng dẫn chạy dự án
1️⃣ Khởi động hệ thống bằng Docker
```bash```
docker compose up -d

2️⃣ Mở Airflow Web UI

URL: http://localhost:8080

Username: admin
Password: admin

3️⃣ Trigger DAG

Enable DAG - Click Trigger DAG

Theo dõi trạng thái trong Graph View

## 11. Ví dụ truy vấn dữ liệu
Kiểm tra số lượng bản ghi

SELECT COUNT(*) FROM fact_sales;

Doanh thu theo chi nhánh

SELECT "Branch", SUM("Total") AS revenue
FROM fact_sales
GROUP BY "Branch";

Doanh thu theo tháng

SELECT DATE_TRUNC('month', "Date") AS month, SUM("Total")
FROM fact_sales
GROUP BY month
ORDER BY month;

## 12. Kết luận

Dự án này minh họa cách xây dựng một ETL pipeline tự động, kiểm soát chất lượng và logging, có sử dụng các công cụ Data Engineering hiện đại.

Pipeline đảm bảo:

Chất lượng và tính nhất quán của dữ liệu

Phân tách rõ ràng các layer xử lý

Dễ dàng orchestration và monitoring bằng Airflow

Khả năng tái tạo hệ thống với Docker

Dữ liệu đầu ra sẵn sàng cho các bài toán phân tích và báo cáo doanh nghiệp.

Có thể cải tiến nâng cao