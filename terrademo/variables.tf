variable "credentials" {
  description = "My credentials"
  default     = "./keys/my-creds.json"

}

variable "project" {
  description = "Project"
  default     = "diesel-octane-416402"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "diesel-octane-416402-terra-bucke"
}


variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}