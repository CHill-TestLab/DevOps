<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>DevOps Skills Tracker</title>
<style>
:root{--bg:#fff;--fg:#1a1a1a;--mut:#666;--card:#f4f5f7;--line:#d5d8dd;--acc:#2563eb;--b:#16a34a;--i:#d97706;--a:#dc2626;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14161a;--fg:#eceef1;--mut:#9aa0a8;--card:#1e2126;--line:#353a42;--acc:#60a5fa;--b:#4ade80;--i:#fbbf24;--a:#f87171}}
:root[data-theme="dark"]{--bg:#14161a;--fg:#eceef1;--mut:#9aa0a8;--card:#1e2126;--line:#353a42;--acc:#60a5fa;--b:#4ade80;--i:#fbbf24;--a:#f87171}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.4 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:960px;margin:0 auto;padding:16px}
h1{font-size:20px;margin:0 0 4px}p.s{color:var(--mut);margin:0 0 12px}
.top{background:var(--card);border-radius:12px;padding:8px;display:grid;grid-template-columns:1fr;gap:8px}
@media(min-width:700px){.top{grid-template-columns:1.2fr 1fr;align-items:center}}
svg{width:100%;max-width:460px;display:block;margin:0 auto}
.sum{padding:8px}.sum .big{font-size:36px;font-weight:700;color:var(--acc)}
.sum table{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}
.sum td{padding:2px 0;border-bottom:1px solid var(--line)}.sum td:last-child{text-align:right;font-variant-numeric:tabular-nums}
.leg{font-size:12px;color:var(--mut);margin:10px 0 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin-top:16px}
details{background:var(--card);border-radius:12px;padding:10px 12px}
summary{cursor:pointer;font-weight:600;display:flex;justify-content:space-between;gap:8px}
summary span{color:var(--acc);font-variant-numeric:tabular-nums;font-weight:500}
label{display:flex;gap:8px;align-items:flex-start;padding:6px 0;cursor:pointer;font-size:14px}
label input{margin-top:1px}
input[type=checkbox]{accent-color:var(--acc);width:18px;height:18px;flex:none}
.task{border-top:1px solid var(--line);padding:4px 0}
.ev{width:100%;box-sizing:border-box;margin:2px 0 0;padding:5px 8px;font:12px system-ui,sans-serif;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:6px}
.bar{display:flex;gap:8px;flex-wrap:wrap}textarea{width:100%;height:120px;box-sizing:border-box;margin-top:8px;font:12px monospace;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:8px}
.t{margin-left:auto;flex:none;font-size:11px;font-weight:700;border:1px solid;border-radius:4px;padding:0 5px}
.t1{color:var(--b)}.t2{color:var(--i)}.t3{color:var(--a)}
button{margin-top:16px;background:none;color:var(--mut);border:1px solid var(--line);border-radius:8px;padding:6px 12px;cursor:pointer}
</style>
</head>
<body>
<main>
<h1>DevOps Skills Tracker</h1>
<p class="s">Paste an evidence link (PR, CI run, screenshot URL) to unlock each task, then tick it. Only tasks with a link count. Harder skills score more.</p>
<div class="top">
<svg id="radar" viewBox="0 0 400 400" role="img" aria-label="Skills radar chart"></svg>
<div class="sum"><div>Overall</div><div class="big" id="ov">0%</div><table id="tb"></table>
<p class="leg"><b class="t1">B</b> Basic = 1pt &nbsp; <b class="t2">I</b> Intermediate = 2pt &nbsp; <b class="t3">A</b> Advanced = 3pt</p></div>
</div>
<div class="grid" id="grid"></div>
<div class="bar"><button id="exp">Export JSON</button><button id="imp">Import JSON</button><button id="reset">Reset all</button></div>
<textarea id="box" style="display:none" aria-label="Export or import JSON"></textarea>
</main>
<script>
const D={
"Linux/CLI":["Find every .log file over 10MB under /var/log with find -size and -exec, and list them with sizes|1","Report the top 10 IP addresses in an nginx access log using only grep, awk, sort and uniq|1","Create a user and group, then set a shared directory to mode 2770 so new files inherit the group|1","Install, upgrade and remove a package, and identify which package owns a given file|1","Find the process holding port 8080 and stop it with SIGTERM before resorting to SIGKILL|1","Set up key-based SSH login, disable password auth in sshd_config, and add a ~/.ssh/config host alias|1","Write a systemd unit that starts a script on boot and restarts on failure, and read its logs with journalctl -u|2","Schedule a nightly job with both cron and a systemd timer, logging output to a file|2","Add a disk, create an LVM volume, format it, and mount it persistently via /etc/fstab|2","Capture traffic on one port with tcpdump and diagnose a failing connection using ss and curl -v|2","Identify whether a slow machine is CPU, memory or I/O bound using top, iostat and strace|3","Fix a SELinux or AppArmor denial by reading the audit log and writing a targeted policy, not disabling it|3"],
"Git":["Create a repo, make three commits on a feature branch, and merge it into main|1","Add a remote, push a branch, and set upstream tracking|1","Open a pull request, get a review, address comments, and merge it|1","Create a merge conflict on purpose and resolve it by hand|1","Use interactive rebase to squash four commits into one and reword the message|2","Use git bisect to locate the commit that introduced a bug, then cherry-pick the fix onto another branch|2","Protect main with required reviews and status checks, and document your branching strategy in the README|2","Write a pre-commit hook that blocks commits failing a linter or secret scan|2","Recover a deleted branch and a commit lost to git reset --hard using git reflog|3","Purge a committed secret from history with git filter-repo and rotate the secret|3"],
"Scripting":["Write a Bash script using a loop and conditional that renames every .txt file in a folder to .bak|1","Extract a nested field from a JSON API response with jq and change a YAML value with yq|1","Write a Python script that reads a CSV and writes summary statistics to a JSON file|1","Run a PowerShell one-liner that lists the 5 most memory-hungry processes and exports them to CSV|1","Write a Bash function and parse -e and -v flags with getopts|2","Write a Bash script with set -euo pipefail and a trap that deletes temp files on failure|2","Write a Python script using requests or boto3 that calls an API with error handling and retries|2","Write a PowerShell function with typed parameters and run it on a remote host|2","Write a regex that extracts timestamps and error codes from logs, used in grep -E or Python|2","Write a script that is safe to run twice with no side effects, plus a bats or pytest test proving it|3"],
"Containers":["Run nginx in a container with a published port, exec into it, and read its logs|1","Write a Dockerfile for a small app, build it, and run it as a non-root user|1","Write a docker-compose.yml running an app and a database with a named volume|1","Tag and push an image to Docker Hub or GHCR, then pull and run it on a different machine|1","Convert a Dockerfile to a multi-stage build and cut the image size by at least 50%|2","Connect two containers by name over a user-defined network and show data persists after container removal|2","Deploy an app to a local Kubernetes cluster (kind or minikube) with 3 replicas and perform a rolling update|2","Expose a deployment via a Service and Ingress, with configuration injected from a ConfigMap|2","Package an app as a Helm chart, then install, upgrade and roll it back|2","Reorder Dockerfile layers so a code-only change rebuilds in under 5 seconds from cache|3","Create a namespace, ServiceAccount and Role that can only read pods, and prove it with kubectl auth can-i|3","Diagnose and fix one CrashLoopBackOff and one ImagePullBackOff pod using describe, logs and events|3","Install an Operator such as cert-manager and create a custom resource it reconciles|3"],
"CI/CD":["Write a pipeline that triggers on every push and builds the project|1","Add a test stage and show it fail on a broken test, then pass after the fix|1","Cache dependencies and upload a build artifact, and show the run time drop|2","Auto-deploy to staging on merge to main, with a manual approval gate before production|2","Store a secret in the CI secret store and use it in a job without it appearing in logs|2","Run a job across a matrix of 3 language versions and call a reusable workflow|2","Tag releases with semantic versions automatically and roll back by redeploying the previous tag|2","Register a self-hosted runner and run a job on it|3","Implement a canary or blue/green deploy that shifts traffic and auto-rolls back on a failed health check|3","Install ArgoCD or Flux, sync a Git repo to a cluster, and undo a change with git revert|3"],
"IaC":["Use Terraform init, plan and apply to create a resource such as a bucket or VM, then destroy it|1","Parameterize a config with variables, locals, outputs and a separate tfvars file per environment|1","Move state to a remote backend with locking and show a second concurrent apply being blocked|2","Write a reusable Terraform module and call it twice with different inputs|2","Deploy dev and prod from one codebase using workspaces or separate state files|2","Write an Ansible playbook and inventory that configures nginx on 2 hosts; a second run reports zero changes|2","Create an Ansible role and encrypt one variable with ansible-vault|2","Import a manually created resource into Terraform state without recreating it|3","Write an OPA, Sentinel or Checkov policy that fails a plan containing a public bucket|3","Add tflint and a Terratest or terraform test suite to your CI pipeline|3","Change a resource by hand, detect the drift with terraform plan, and reconcile it|3"],
"Cloud":["Launch a VM, SSH in, install a web server, reach it via public IP, then terminate it|1","Configure an autoscaling group that adds an instance when CPU passes a threshold|1","Upload a file to object storage, share it via a time-limited signed URL, and add a lifecycle rule|1","List and create a resource using both the cloud CLI and an SDK script|1","Build a VPC with public and private subnets, and show the private host has outbound-only internet via NAT|2","Create an IAM role limited to one bucket and assume it from a VM or the CLI|2","Launch a managed database in a private subnet, connect from an app VM, and enable automated backups|2","Deploy a serverless function triggered by HTTP or a queue and read its logs|2","Create a managed Kubernetes cluster (EKS, AKS or GKE) and deploy an app to it|2","Set a budget alert, identify your top 3 cost drivers, and delete unused resources|2","Set up a multi-account or subscription structure with an org-level policy denying a region or action|3","Run a failover drill by restoring a database from backup in another zone or region and recording the recovery time|3"],
"Networking":["Trace one request from browser to server, naming each protocol layer, verified with curl -v and traceroute|1","Split 10.0.0.0/16 into four /24 subnets by hand and state the usable hosts in each|1","Create A, CNAME and MX records and trace resolution with dig +trace|1","Send GET, POST and PUT with curl and explain a 301, 401, 403, 404, 502 and 503 response|1","Issue a certificate with Let's Encrypt or openssl, install it, and inspect the chain with openssl s_client|2","Put a load balancer with health checks in front of 2 servers and show traffic continues when one is stopped|2","Write firewall rules allowing SSH only from your IP and HTTPS from anywhere, verified with nmap|2","Connect two hosts with a WireGuard or site-to-site VPN and ping across it|2","Configure nginx or HAProxy as a reverse proxy with TLS termination and path-based routing|2","Install Istio or Linkerd, enable mTLS between two services, and view traffic metrics|3","Capture a TCP handshake and a TLS handshake in Wireshark and annotate the packets|3"],
"Monitoring":["Find all errors in the last hour of an app's logs using journalctl --since or grep|1","Install Prometheus, scrape node_exporter, and run a PromQL query for CPU usage|2","Build a Grafana dashboard with 4 panels: CPU, memory, disk and request rate|2","Write an alert firing when disk is over 85% for 5 minutes, routed to Slack or email via Alertmanager|2","Deploy Loki or ELK, ship logs from 2 services, and filter by label or field|2","Set up an external uptime check that alerts you when the endpoint goes down|2","Run an on-call drill: acknowledge an alert, diagnose, resolve, and keep timeline notes|2","Write a blameless postmortem with timeline, root cause and 3 action items|2","Instrument an app with OpenTelemetry and view one trace spanning two services in Jaeger or Tempo|3","Define an SLI and 99.9% SLO, calculate the error budget, and create a burn-rate alert|3"],
"Security":["Store a secret in Vault or a cloud secrets manager and fetch it at runtime with nothing in code or env files|1","Audit one IAM role or user, remove an unneeded permission, and confirm nothing breaks|1","Disable SSH password and root login, and rotate an SSH key|1","Run npm audit, pip-audit or Dependabot and fix one vulnerable dependency|2","Scan an image with Trivy or Grype and fix a HIGH severity finding|2","Restrict a database so only the app tier can reach it, and prove other hosts are blocked|2","Apply OS security updates on 2 or more servers and verify with a patch report or unattended-upgrades|2","Add SAST (CodeQL or Semgrep) to CI and show it failing the build on a seeded vulnerability|3","Generate an SBOM with Syft and rebuild on a distroless or minimal base image|3","Enable cloud audit logging and query it for one specific user action|3","Write a STRIDE threat model for a small app listing 5 threats and their mitigations|3"]};
const K="devops-skills-v4";let S={},E={};
try{const o=JSON.parse(localStorage.getItem(K)||"{}");S=o.S||{};E=o.E||{}}catch(e){}
const ok=u=>/^https?:\/\/\S+$/i.test((u||"").trim()),done=k=>!!S[k]&&ok((E[k]||{}).u),esc=x=>String(x).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;");
const names=Object.keys(D),N=names.length,grid=document.getElementById("grid"),L=["","B","I","A"];
names.forEach((n,i)=>{const d=document.createElement("details");d.open=false;
d.innerHTML=`<summary>${n}<span id="p${i}"></span></summary>`+D[n].map((s,j)=>{const[t,l]=s.split("|"),k=i+"-"+j,e=E[k]||{};return `<div class="task"><label><input type="checkbox" data-k="${k}" ${done(k)?"checked":""} ${ok(e.u)?"":"disabled"}>${t}<b class="t t${l}">${L[l]}</b></label><input class="ev" data-k="${k}" data-f="u" placeholder="Evidence URL (PR, CI run, screenshot...)" value="${esc(e.u||"")}"><input class="ev" data-k="${k}" data-f="n" placeholder="Notes" value="${esc(e.n||"")}"></div>`}).join("");
grid.appendChild(d)});
function sc(i){let g=0,m=0,c=0;D[names[i]].forEach((s,j)=>{const w=+s.split("|")[1];m+=w;if(done(i+"-"+j)){g+=w;c++}});return{p:g/m,c,n:D[names[i]].length,g,m}}
function draw(){
const cx=200,cy=200,R=120,pt=(i,r)=>{const a=-Math.PI/2+2*Math.PI*i/N;return[cx+r*Math.cos(a),cy+r*Math.sin(a)]};
let h="";
[.25,.5,.75,1].forEach(f=>{h+=`<polygon points="${names.map((_,i)=>pt(i,R*f).join(",")).join(" ")}" fill="none" stroke="var(--line)"/>`});
names.forEach((n,i)=>{const[x,y]=pt(i,R),[lx,ly]=pt(i,R+16);
h+=`<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="var(--line)"/>`;
const an=Math.abs(lx-cx)<8?"middle":lx>cx?"start":"end";
h+=`<text x="${lx}" y="${ly+4}" text-anchor="${an}" font-size="12" fill="var(--fg)">${n}</text>`});
const R2=names.map((_,i)=>sc(i)),P=R2.map((s,i)=>pt(i,R*s.p));
h+=`<polygon points="${P.map(p=>p.join(",")).join(" ")}" fill="var(--acc)" fill-opacity=".3" stroke="var(--acc)" stroke-width="2"/>`;
P.forEach(p=>{h+=`<circle cx="${p[0]}" cy="${p[1]}" r="3" fill="var(--acc)"/>`});
document.getElementById("radar").innerHTML=h;
let G=0,M=0,rows="";
R2.forEach((s,i)=>{G+=s.g;M+=s.m;const t=Math.round(s.p*100)+"%";document.getElementById("p"+i).textContent=s.c+"/"+s.n+" · "+t;rows+=`<tr><td>${names[i]}</td><td>${t}</td></tr>`});
document.getElementById("tb").innerHTML=rows;
document.getElementById("ov").textContent=Math.round(G/M*100)+"%"}
function save(){try{localStorage.setItem(K,JSON.stringify({S,E}))}catch(e){}}
grid.addEventListener("input",e=>{const t=e.target;if(!t.classList.contains("ev"))return;const k=t.dataset.k;(E[k]=E[k]||{})[t.dataset.f]=t.value;
if(t.dataset.f==="u"){const cb=grid.querySelector(`input[type=checkbox][data-k="${k}"]`),v=ok(t.value);cb.disabled=!v;if(!v){S[k]=false;cb.checked=false}}save();draw()});
grid.addEventListener("change",e=>{if(e.target.type==="checkbox"){S[e.target.dataset.k]=e.target.checked;save();draw()}});
const box=document.getElementById("box");
document.getElementById("exp").onclick=()=>{const o=[];names.forEach((n,i)=>D[n].forEach((s,j)=>{const k=i+"-"+j,e=E[k]||{};if(e.u||e.n||S[k]){const[t,l]=s.split("|");o.push({area:n,task:t,level:+l,done:done(k),evidence:e.u||"",notes:e.n||""})}}));
box.value=JSON.stringify(o,null,2);box.style.display="block";box.select();try{navigator.clipboard.writeText(box.value)}catch(x){}};
document.getElementById("imp").onclick=()=>{if(box.style.display!=="block"){box.style.display="block";box.value="";box.placeholder="Paste exported JSON here, then click Import again";return}
try{const o=JSON.parse(box.value);names.forEach((n,i)=>D[n].forEach((s,j)=>{const m=o.find(r=>r.area===n&&r.task===s.split("|")[0]);if(m){const k=i+"-"+j;E[k]={u:m.evidence||"",n:m.notes||""};S[k]=!!m.done}}));save();location.reload()}catch(x){box.value="Invalid JSON"}};
document.getElementById("reset").onclick=()=>{if(confirm("Clear all progress and evidence?")){S={};E={};save();location.reload()}};
draw();
</script>
</body>
</html>
