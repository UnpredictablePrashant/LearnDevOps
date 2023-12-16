# templates/_helpers.tpl
{{/* Define a default "fullname" if not set */}}
{{- define "my-nodejs-app-chart.fullname" -}}
{{- default .Chart.Name .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}
