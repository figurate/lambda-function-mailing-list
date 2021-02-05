# Serverless Mailing List

A simple mailing list subscription manager.

## DynamoDB

| PK                        | SK                      | Name         | Subscription Date |
|---------------------------|-------------------------|--------------|-------------------|
| SUBSCRIBER#s1@example.com | #PROFILE#s1@example.com | Subscriber 1 | -                 |
| SUBSCRIBER#s1@example.com | LIST#1                  | -            | 01/01/2020        |
| LIST#1                    | #PROFILE#1              | List 1       | -                 |
