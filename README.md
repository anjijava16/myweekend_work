# myweekend_work

# Reference's
1. https://github.com/aws-samples/emr-on-eks-hudi-iceberg-delta/blob/main/hudi/hudi_scd_script.py
2. https://aws.amazon.com/blogs/big-data/get-a-quick-start-with-apache-hudi-apache-iceberg-and-delta-lake-with-amazon-emr-on-eks/
3. https://aws.amazon.com/blogs/big-data/build-slowly-changing-dimensions-type-2-scd2-with-apache-spark-and-apache-hudi-on-amazon-emr/
4. https://iomete.com/blog/cheat-sheet-for-apache-iceberg
5. https://bigdataboutique.com/blog/introduction-to-apache-hudi-c83367
6. https://www.tencentcloud.com/document/product/1026/35587
7. https://github.com/vasveena/DemoNotes
8. https://medium.com/@parveen.jindal/having-your-cake-and-eating-it-too-how-vizio-built-a-next-generation-data-platform-to-enable-bi-4fc42c539543

# Weekend work
1. Create a EMR Cluster (should be 6.10)
2. Connect to SSH
3. Check Table Format all required Jars
4. Understand Iceberg Files
5. Understand Hudi Files
6. Understand Delta Lake Files
7. Create a MYSQL DB (create Retail_DB)
8. Copy MYSQL DB to S3 as Parquet Files
9. Source as : S3 Parquet 

# Flow Like below
1. MYSQL ---> (Spark Read as Files)  ---> Write as S3 Files
2. S3 Read Files ---> Write as Hudi FS 
3. S3 Read Files ---> Write to Iceberg
4. S3 Read Files ----> Write to HUDI

# Clean process
1. Terminate EMR Cluster
2. Terminate EMR S3 Logs


# Next Steps
1. Create FastAPi Microservice ---> Configure Read as JDBC MYSQL Table ---> Write to S3 ---> Write to S3 Different Table Format FS

## Do some experments on Livy Server on EMR 



