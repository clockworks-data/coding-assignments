# Clockworks Coding Assignment - Using our API
You are given a partially implemented system which, given a list of images, should categorize the images into one of the following:

- Gas
- Water
- Electric
- Unknown

The images are given as a list of URLs. To categorize these images the Clockworks Meter Reading API is to be used (see [Clockworks Meter Reading API](clockworks-meter-reading-api) for instructions).

The aggregated statistics (total number of gas, water, electric, or unknown meters detected) should be reported in a web-based interface.

We have provided a starting point with some of the functionality already implemented using Docker containers. These containers can be deployed locally using docker-compose (see [Getting Started](getting-started])).

Your goal is to complete our implementation.

In the end-state the system should consist of at least the following components:

- **Message Broker** - The Kafka message broker that can be used for communication between components.
- **Producer** - Responsible for periodically sending URLs on the message bus.
- **Consumer** - Consumes URLs from the producer and should use the Clockworks Meter Reading API to find out whether or not the image at the URL is a gas, water, electric, or unknown meter. *Note: this component is only partially implemented.*
- **Frontend** - Web-based frontend that shows aggregated statistics of the processed URLs (number of gas, water, electric, or unknown meters detected). *Note: this component is not yet implemented.*

## Notes
- The consumer should be written in Python
- The web-based frontend can be implemented in any technology of your choosing as long as it is accessible using a browser after firing up the Docker containers
- Styling of the frontend is not important
- If you are stuck on something do not hesistate to reach out!

## Getting Started
Execute the following command to get started:
```
$ docker-compose up
```

Initially, after all containers are started should see the producer and consumer outputting URLs.

## Clockworks Meter Reading API

Below is a short introduction on how to use our API. See *swagger.json* for the complete documentation.

- **URL** - https://api.clockworks.co
- **Subscription Key** - *you should have received this alongside with the assignment*

**API usage using CURL**

Using the subscription key as a GET parameter:

```bash
$ curl -X POST --form "image=@image.jpg" "https://api.clockworks.co/full_meter?subscription-key=<SUBSCRIPTION_KEY>"
```

Using the subscription key as a header:

```bash
$ curl -X POST --form "image=@image.jpg" --header "Subscription-Key: <SUBSCRIPTION_KEY>" "https://api.clockworks.co/full_meter"
```
**Example API Output**

The API output contains a JSON object as follows. You should use the *metercategory* field for the categorization.

```json
{
    "bad_photo": false,
    "barcode": [],
    "display": [
        {
            "bbox": [
                108,
                484,
                371,
                527
            ],
            "confidence": 0.68,
            "uncertain": false,
            "value": "55437,162"
        }
    ],
    "messages": [],
    "metercategory": "gas",
    "metercategory_confidence": 1.0,
    "metercode": "unknown",
    "metercode_confidence": 1.0,
    "meternummer": [
        {
            "bbox": [
                269,
                535,
                437,
                567
            ],
            "confidence": 0.72,
            "uncertain": false,
            "value": "34118729"
        }
    ],
    "warnings": false
}
```

