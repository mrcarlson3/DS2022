#!/bin/bash

curl https://www.cabq.gov/artsculture/biopark/news/10-cool-facts-about-penguins/@@images/1a36b305-412d-405e-a38b-0947ce6709ba.jpeg > fluff.jpeg

aws s3 cp fluff.jpeg s3://ds2022-mjy7nw/

aws s3 presign --expires-in 604800  s3://ds2022-mjy7nw/fluff.jpeg

# https://ds2022-mjy7nw.s3.us-east-1.amazonaws.com/fluff.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA6IY36ALUF7HDEIRC%2F20241002%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241002T182353Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d0642ee180f6028995575561c54969535a675617853c51c2bd1d5b064d1e92f3 
