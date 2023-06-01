import aws_cdk as core
import aws_cdk.assertions as assertions

from ctcwl_oss.ctcwl_oss_stack import CtcwlOssStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ctcwl_oss/ctcwl_oss_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CtcwlOssStack(app, "ctcwl-oss")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
