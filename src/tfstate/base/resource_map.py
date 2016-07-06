# -*- coding: utf-8 -*-

# tfstate
from tfstate.provider import aws, other


class ResourceMap(object):
    """
    Class to map the resource names from a tfstate to the Resource classes
    """

    RESOURCE_MAP = {
        'aws_eip': aws.AwsEipResource,
        'aws_elb': aws.AwsElbResource,
        'aws_iam_server_certificate': aws.AwsIamServerCertificateResource,
        'aws_instance': aws.AwsInstanceResource,
        'aws_internet_gateway': aws.AwsInternetGatewayResource,
        'aws_key_pair': aws.AwsKeyPairResource,
        'aws_nat_gateway': aws.AwsNatGatewayResource,
        'aws_route': aws.AwsRouteResource,
        'aws_route_table': aws.AwsRouteTableResource,
        'aws_route_table_association': aws.AwsRouteTableAssociationResource,
        'aws_security_group': aws.AwsSecurityGroupResource,
        'aws_security_group_rule': aws.AwsSecurityGroupRuleResource,
        'aws_subnet': aws.AwsSubnetResource,
        'aws_vpc': aws.AwsVpcResource,
        'aws_vpc_peering_connection': aws.AwsVpcPeeringConnectionResource,
        'null_resource': other.NullResource,
    }

    @staticmethod
    def get(resource_name):
        """
        Retrieve a class given its tfstate resource name

        :param str resource_name: Resource name to look up
        :raises NotImplementedError: If a resource is not implemented yet
        """

        resource_type = resource_name.split('.')[0]
        resource_class = ResourceMap.RESOURCE_MAP.get(resource_type, None)
        if resource_class is None:
            raise NotImplementedError('Resource {} not implemented yet'.format(resource_name))

        return resource_class
