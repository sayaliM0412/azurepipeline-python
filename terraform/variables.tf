variable "region" {
  default = "us-west-2"
}

locals {
    env_name =lower(terraform.workspace)

common_tags = {
  Environment = local.env_name
}

}