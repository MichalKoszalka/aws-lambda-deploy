
## Installation
Please ensure you have the [AWS CLI](https://aws.amazon.com/cli) installed and configured with [credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

The install script uses SAM to deploy relevant resources to your AWS account:
```bash
$ ./install.sh
```

## Passing flow
```bash
$ ./successfull-canary.sh
```

## Failing flow

```bash
$ ./failed-canary.sh
```
