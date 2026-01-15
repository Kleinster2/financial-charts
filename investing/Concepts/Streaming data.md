# Streaming data

Real-time data processing as an alternative to batch ETL — processing events as they happen rather than in scheduled batches.

## Theory

**Batch processing (traditional):**
- Data collected, processed on schedule (hourly, daily)
- Simpler, cheaper, sufficient for most analytics
- Latency: minutes to hours

**Stream processing:**
- Data processed continuously as it arrives
- Lower latency (milliseconds to seconds)
- More complex, higher infrastructure cost
- Required for real-time use cases

## Key technologies

| Technology | Type | Notes |
|------------|------|-------|
| Apache Kafka | Message broker | De facto standard, LinkedIn origin |
| Confluent | Kafka vendor | Public (CFLT), Kafka creators' company |
| Apache Flink | Stream processing | Growing, Alibaba/AWS backing |
| Apache Spark Streaming | Stream processing | [[Databricks]] ecosystem |
| Amazon Kinesis | Managed streaming | AWS-native alternative |
| Redpanda | Kafka alternative | Faster, C++ rewrite, private |

## Confluent deep dive

- **Ticker:** CFLT
- **Thesis:** Kafka is infrastructure standard, Confluent monetizes
- **Bull:** streaming adoption growing, cloud Kafka sticky
- **Bear:** AWS Kinesis/MSK competition, open source Kafka free
- **Watch:** cloud revenue growth, retention metrics

## Use cases driving adoption

- Fraud detection (financial services)
- Real-time recommendations (e-commerce)
- IoT sensor processing
- Log aggregation / observability
- Event-driven microservices

## Investment implications

| Dynamic | Effect |
|---------|--------|
| Streaming ≠ batch replacement | Most workloads stay batch, streaming is additive |
| Kafka dominance | Confluent benefits but faces cloud competition |
| Complexity tax | Streaming harder to operate, limits adoption |
| Flink rising | May challenge Spark for stream processing |

## Thesis considerations

- Confluent (CFLT) is the direct streaming play
- Streaming infrastructure is necessary but not sufficient
- Watch for [[Databricks]] vs Flink dynamics
- Real-time AI inference could accelerate streaming demand

## Related

- [[Databases]] — streaming feeds into analytical stores
- [[Modern data stack]] — streaming as ingestion alternative
- [[Data lakehouse]] — destination for streaming data
