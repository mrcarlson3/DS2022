#!/bin/bash

curl https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMYGAiWWkQeEvx5Y-eKQ5iT0ZFzHhV-mE3EQ&s > pesto.jpeg

aws s3 cp pesto.jpeg s3://ds2022-mjy7nw/

aws s3 presign --expires-in 604800  s3://ds2022-mjy7nw/pesto.jpeg

https://ds2022-mjy7nw.s3.us-east-1.amazonaws.com/pesto.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA6IY36ALUF7HDEIRC%2F20240927%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240927T171916Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fa7a9f438f52447505e2e035995eabb5a4df7165540ec7579e09cb75d14ffe56
