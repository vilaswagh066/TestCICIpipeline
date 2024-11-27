import requests
import argparse

def deploy_pipeline(base_url, org, project, env, auth_token, pipeline_file):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    url = f"{base_url}/api/1/rest/public/project/{org}/{project}/pipeline/{env}"
    with open(pipeline_file, 'r') as file:
        payload = file.read()
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Successfully deployed pipeline: {pipeline_file}")
    else:
        print(f"Failed to deploy {pipeline_file}: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth-token", required=True)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--org", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--env", required=True)
    args = parser.parse_args()

    deploy_pipeline(args.base_url, args.org, args.project, args.env, args.auth_token, "path/to/your/pipeline.json")
