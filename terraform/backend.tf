terraform {
  required_version = "0.13.4"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "TrialRUn"
    workspaces {
      prefix = "sys75-"
    }
  }
}