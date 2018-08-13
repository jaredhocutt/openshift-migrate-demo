# OpenShift Migrate

## Demo

```bash
ansible-playbook playbooks/setup.yml

ansible-playbook playbooks/deploy_dev.yml

ansible-playbook playbooks/deploy_prod.yml

ansible-playbook playbooks/migrate_app.yml
```

## Teardown

```bash
ansible-playbook playbooks/teardown.yml
```
