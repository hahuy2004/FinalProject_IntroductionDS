# FINAL PROJECT - INTRODUCTION TO DATA SCIENCE
---
## 1. Thông tin nhóm 10

| **STT** | **Họ và tên** | **MSSV** |
|-------|---------------|---------|
| 1     | Trần Gia Hào | 22120099 |
| 2     | Nguyễn Minh Hưng | 22120123 |
| 3     | Nguyễn Tấn Hưng | 221200126 |
| 4     | Hà Đức Huy | 22120133 |
| 5     | Trần Duy Khang | 22120153 |

---
## 2. Tổng quan đề tài
- Manga, Manhua, Manhwa, Light-novel và các thể loại truyện khác là những hình thức nghệ thuật kể chuyện độc đáo, đại diện cho các nền văn hóa đa dạng từ Nhật Bản, Trung Quốc, Hàn Quốc và các tác giả quốc tế. Không chỉ dừng lại ở vai trò giải trí, các tác phẩm này đã trở thành cầu nối văn hóa, phản ánh xã hội, tư tưởng, và những giá trị sâu sắc thông qua các câu chuyện hấp dẫn và phong cách nghệ thuật đặc sắc.
- Sự bùng nổ của các nền tảng như `MyAnimeList (MAL)`, `Anime-Planet`, hay các website đọc truyện trực tuyến đã mở ra cơ hội lớn để phân tích dữ liệu và khám phá xu hướng của thị trường màu mỡ này. Các thông tin về thể loại, đánh giá người dùng, số lượng độc giả, và mức độ phổ biến của từng tác phẩm đều là những chỉ số quan trọng giúp hiểu rõ hơn về ngành công nghiệp truyện tranh và tiểu thuyết.
- Phân tích dữ liệu từ các nguồn này không chỉ giúp chúng ta hiểu sâu sắc hơn về sở thích của độc giả, nghiên cứu văn hóa và xã hội, cũng như dữ đoán xu hướng phát triển các thể loại truyện trong tương lai.
---
## 3. Chi tiết thư hiện
- **Chủ đề:** Các thể loại truyện (Manga, Manhua, Manhwa, Light Novel, ...)
- **Nơi thu thập:** MyAnimeList
- **Tổng quan thực hiện:** Nhóm thực hiện các bước sau:
  - Data Collecting: Thu thập dữ liệu từ trang [All Manga](https://myanimelist.net/topmanga.php) của `MyAnimeList`.
  - Data Preprocessing: Xử lí dữ liệu để cho dữ liệu tốt hơn.
  - Data Exploring: Khám phá tổng quan bộ dữ liệu, tìm hiểu phân phối của từng thuộc tính.
  - Data Visualization: Trực quan hóa dữ liệu dựa trên những câu hỏi được đặt ra.
  - Data Modeling: Đặt ra những vấn đề giải quyết bằng các mô hình, xây dựng hệ thống Recommendation các bộ truyện.
---
## 4. Tổ chức GitHub
```
├── README.md                                                           <- Mô tả về đồ án.
│
├── Final_Project                                                       <- Folder chứa data và code.
│   ├── data                                                            <- Folder chứa dữ liệu.
│   │    ├── README.md                                                  <- Mô tả thư mục data.
│   │    ├── link_collecting_1.txt                                      <- File .txt chứa đường link về các trang thông tin của từng bộ truyện.
│   │    ├── ...                                                        <- Tương tự với link_collecting_2.txt, link_collecting_3.txt, link_collecting_4.txt.
│   │    ├── manga_processed.csv                                        <- Dữ liệu đã được xử lý.
│   │    ├── raw_manga.csv                                              <- Dữ liệu thô được thu thập từ trang web.
│   ├── source                                                          <- Folder chứa các file notebook và code thực thi.
│   │    ├── README.md                                                  <- Mô tả thư mục source.
│   │    ├── data_collecting.ipynb                                      <- Notebook Data Collecting.
│   │    ├── data_preprocessing.ipynb                                   <- Notebook Data Preprocessing.
│   │    ├── data_exploring.ipynb                                       <- Notebook Data Exploring.
│   │    ├── data_visualization.ipynb                                   <- Notebook Data Visualization.
│   │    ├── data_modeling_regression_{...}.ipynb                       <- Notebook Data Modeling Regression: Dự đoán điểm số dựa trên dữ liệu mẫu.
│   │    ├── data_modeling_demographic_classifier_{...}.ipynb           <- Notebook Data Modeling Classification: Phân loại truyện dựa trên đối tượng độc giả.
│   │    ├── manga_searching_recommedation_system.ipynb                 <- Notebook Modeling System: Hệ thống Recommendation các bộ truyện.
│   │    ├── merge_manga.py                                             <- Source code ghép các dữ liệu thành phần để tạo ra dữ liệu raw_manga.csv, hỗ trợ cho thao tác Data Collecting.
│
├── CSC14119_CQ22_FinalProject                                          <- Mô tả về đồ án cuối kì NMKHDL.
|
├── Slide.pdf                                                           <- Slide báo cáo cuối kì.
```
---
##  5. Khó khăn và hướng giải quyết
- **Khó khăn:**
  - Trang web giới hạn số lượng requests khiến việc thu thập dữ liệu trở nên khó khăn
  - Khó khăn trong việc đánh giá và quyết định xử lý từng cột thuộc tính trong bộ dữ liệu như thế nào, điền các giá trị bị thiếu trong từng cột theo giá trị gì, ...
  - Đặt những câu hỏi có ý nghĩa là một vấn đề nan giải và thách thức với nhóm
  - Việc lên ý tưởng, sử dụng và tinh chỉnh các mô hình để giải quyết các vấn đề phân lớp, hồi quy trong bộ dữ liệu gây khó khăn cho thành viên trong nhóm do chưa có nhiều kinh nghiệm về Machine Learning, Deep Learning,...
- **Hướng giải quyết:**
  - Chia nhỏ các phần cần thu thập thành nhiều file notebook thực thi cùng một lúc. Sau khi thu thập đủ dữ liệu, tiến hành ghép dữ liệu để tạo thành bộ hoàn chỉnh.
  - Nhóm đã thảo luận với nhau và đưa ra các quyết định về việc xử lý và khai phá dữ liệu
  - Về việc xây dựng mô hình, các thành viên được giao nhiệm vụ đã cố gắng tìm hiểu về các mô hình, cũng như cách thức áp dụng chúng vào trong các bài toán cần sử dụng mô hình để dự đoán, phân lớp
  - Nhóm đã đọc và tìm hiểu kĩ từng thuộc tính của dữ liệu được thu thập, đồng thời cũng tìm hiểu và tham khảo xu hướng người dùng, nhà sản xuất, cũng như từng chuyển biến của Manga, Manhwa, Manhua, Light Novel, Novel, Oneshot, Doujinshi trên thế giới thông qua các mạng xã hội như YouTube, Facebook, X,... để có thể đưa ra những câu hỏi có ý nghĩa và phù hợp với xu hướng hiện nay.
  - Nhóm cũng tích cực trao đổi trên nhóm chat riêng, cũng như thông qua Github để nắm được tiến độ làm việc của nhau cũng như hiểu biết về phần việc của từng thành viên rõ hơn.
---

---
##  6. Suy nghĩ và đánh giá đồ án:
- **Những điều học được từ đồ án này:**
  - Học cách thu thập dữ liệu bằng công cụ như requests, BeautifulSoup, Selenium,...
  - Học được cách tiền xử lý và khai phá dữ liệu như xử lý dữ liệu bị thiếu, nhập xuất dữ liệu từ tập tin, kiểm tra kiểu dữ liệu các thuộc tính, ...
  - Học được cách trực quan hóa bằng thư viện và nắm được cách đặt những câu hỏi có ý nghĩa dựa trên bộ dữ liệu hiện có
  - Học được cách lên ý tưởng, sử dụng và tinh chỉnh các mô hình để giải quyết các vấn đề phân lớp, hồi quy trong bộ dữ liệu
  - Học được cách phối hợp nhóm, thuyết trình, cũng như sử dụng GitHub để quản lý đồ án.
 
- **Nếu còn thời gian, nhóm sẽ thực hiện những điều sau:**
  - Nhóm sẽ tìm hiểu sâu hơn về phân phối và ý nghĩa của từng thuộc tính trong bộ dữ liệu. Đồng thời áp dụng các phương pháp xử lý dữ liệu tốt hơn.
  - Đặt nhiều câu hỏi có ý nghĩa hơn, do hiện tại vẫn còn một vài câu mang tính khai thác mối quan hệ dữ liệu hơn là trả lời về một chủ đề gì đó.
  - Sử dụng các phương pháp, các mô hình tốt hơn để áp dụng cho các vấn đề liên quan đến hồi quy, phân lớp.
  - Cải thiện hệ thống Recommendation cho các bộ truyện tốt hơn.
 
---

## 7. Không gian làm việc
- Link Group Working: [Group Working](https://docs.google.com/spreadsheets/d/1hQfAfnTYzPI49zXJ3Qhi1Cc8cTE-MGoR/edit?usp=sharing&ouid=102314169989540342274&rtpof=true&sd=true)
- Link Slide Canva: [Slide](https://www.canva.com/design/DAGZhXrDbUY/dSej6HkqXELjl3I9LKJbbQ/edit)

