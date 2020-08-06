from aws_cdk import core
import yaml



class AwscdktestStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        iam_role_template = core.CfnParameter(self, "iamRoleTemplate", type="String",
        description="template name for iam saml role.")
        
        core.CfnInclude(self, "ExistingInfrastructure",
    	template=yaml.load(open(iam_role_template.value_as_string),Loader=yaml.FullLoader))
 
        iam_developer_role = core.CfnInclude(self, "IamDeveloperRole",
        	template=yaml.load(open(iam_role_template.value_as_string),Loader=yaml.FullLoader))

       