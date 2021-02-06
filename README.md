# Serverless Subscriber List

A simple subscription manager.

## Overview

Subscriber lists are useful to maintain a list of active users, resources, or anything that may be the target of
a collective action. Examples include mailing/distribution lists, user groups, inventory, etc.

### Subscription Type

A subscription type is an arbitrary identifier to ensure consistency of a subscriber list. For example, a list with
subscription type = `email` should only accept subscribers where the subscriber id is an email address.

### Suspended subscriptions

A subscription may also be suspended to exclude it from any action taken on the subscriber list without removing
it from the list (unsubscribing). A common use case is to create new subscriptions in a suspended state until
activated via some form of verification of the subscriber.

## Specification

### DynamoDB

| PK                        | SK                      | Name         | Subscription Date | Suspended | Subscriber Type |
|---------------------------|-------------------------|--------------|-------------------|-----------|-----------------|
| SUBSCRIBER#s1@example.com | #PROFILE#s1@example.com | Subscriber 1 | -                 |           | -               |
| SUBSCRIBER#s1@example.com | LIST#1                  | -            | 01/01/2020        | false     | -               |
| LIST#1                    | #PROFILE#1              | List 1       | -                 |           | email           |
