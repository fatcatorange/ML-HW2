# 使用基礎映像（例如Python）
FROM python:3.9

# 設定工作目錄
WORKDIR /ml-HW2

# 複製所需文件到容器中
COPY . .


# 安裝所需依賴
RUN pip install -r requirements.txt

# 設置ENTRYPOINT為啟動cmd
CMD ["bash"]
