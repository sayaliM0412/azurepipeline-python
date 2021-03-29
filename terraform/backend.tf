terraform {
  required_version = "0.14.9"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "TrialRUn"
    workspaces {
      prefix = "sys75-"
    }
  }
}


provider "tfe" {
  hostname = "app.terraform.io"
}
