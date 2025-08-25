# Script para Assinatura Digital do Executável
# Este script pode ser usado para assinar digitalmente o executável
# quando um certificado de código estiver disponível

param(
  [Parameter(Mandatory = $true)]
  [string]$ExecutablePath,
    
  [Parameter(Mandatory = $false)]
  [string]$CertificateThumbprint = "",
    
  [Parameter(Mandatory = $false)]
  [string]$CertificateStore = "My",
    
  [Parameter(Mandatory = $false)]
  [string]$TimestampUrl = "http://timestamp.digicert.com"
)

Write-Host "Script de Assinatura Digital - Ordem do Dia" -ForegroundColor Cyan
Write-Host ("=" * 50)

# Verificar se o executável existe
if (-not (Test-Path $ExecutablePath)) {
  Write-Error "Executavel nao encontrado: $ExecutablePath"
  exit 1
}

Write-Host "Executavel: $ExecutablePath" -ForegroundColor Green

# Verificar se temos certificado disponível
if ([string]::IsNullOrEmpty($CertificateThumbprint)) {
  Write-Host "Nenhum certificado especificado - pulando assinatura" -ForegroundColor Yellow
  Write-Host "Para assinar o executavel:" -ForegroundColor Cyan
  Write-Host "   1. Obtenha um certificado de codigo valido" -ForegroundColor White
  Write-Host "   2. Execute: .\sign_executable.ps1 -ExecutablePath '$ExecutablePath' -CertificateThumbprint 'THUMBPRINT'" -ForegroundColor White
  # Mesmo sem assinatura, vamos criar informacoes uteis
  Write-Host ("`nInformacoes do Executavel:") -ForegroundColor Cyan
  $fileInfo = Get-Item $ExecutablePath
  Write-Host "   Criado: $($fileInfo.CreationTime)" -ForegroundColor White
  Write-Host "   Tamanho: $([math]::Round($fileInfo.Length / 1MB, 2)) MB" -ForegroundColor White
  $hash = Get-FileHash $ExecutablePath -Algorithm SHA256
  Write-Host "   SHA256: $($hash.Hash)" -ForegroundColor White
  # Salvar hash para verificacao
  $hashFile = "$ExecutablePath.sha256"
  $hash.Hash | Out-File $hashFile -Encoding UTF8
  Write-Host "   Hash salvo em: $hashFile" -ForegroundColor Green
  Write-Host ("`nVerificacao concluida (sem assinatura)") -ForegroundColor Green
  exit 0
}

# Tentar encontrar o certificado
try {
  $cert = Get-ChildItem "Cert:\CurrentUser\$CertificateStore" | Where-Object { $_.Thumbprint -eq $CertificateThumbprint }
  if (-not $cert) {
    $cert = Get-ChildItem "Cert:\LocalMachine\$CertificateStore" | Where-Object { $_.Thumbprint -eq $CertificateThumbprint }
  }
  if (-not $cert) {
    Write-Error "Certificado nao encontrado: $CertificateThumbprint"
    exit 1
  }
  Write-Host "Certificado encontrado: $($cert.Subject)" -ForegroundColor Green
} catch {
  Write-Error "Erro ao buscar certificado: $($_.Exception.Message)"
  exit 1
}

# Verificar se o SignTool está disponível
$signTool = Get-Command "signtool.exe" -ErrorAction SilentlyContinue
if (-not $signTool) {
  Write-Host "SignTool nao encontrado - tentando localizar..." -ForegroundColor Yellow
  # Caminhos comuns do SignTool
  $possiblePaths = @(
    "${env:ProgramFiles(x86)}\Windows Kits\10\bin\*\x64\signtool.exe",
    "${env:ProgramFiles}\Windows Kits\10\bin\*\x64\signtool.exe",
    "${env:ProgramFiles(x86)}\Microsoft SDKs\Windows\*\bin\signtool.exe"
  )
  foreach ($path in $possiblePaths) {
    $found = Get-ChildItem $path -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($found) {
      $signTool = $found.FullName
      Write-Host "SignTool encontrado: $signTool" -ForegroundColor Green
      break
    }
  }
  if (-not $signTool) {
    Write-Error "SignTool nao encontrado. Instale o Windows SDK."
    exit 1
  }
} else {
  $signTool = $signTool.Path
}

# Assinar o executável
try {
  Write-Host "Assinando executavel..." -ForegroundColor Cyan
  $signArgs = @(
    "sign",
    "/sha1", $CertificateThumbprint,
    "/t", $TimestampUrl,
    "/fd", "SHA256",
    "/v",
    "`"$ExecutablePath`""
  )
  $result = & $signTool $signArgs
  if ($LASTEXITCODE -eq 0) {
    Write-Host "Executavel assinado com sucesso!" -ForegroundColor Green
    # Verificar assinatura
    Write-Host "Verificando assinatura..." -ForegroundColor Cyan
    $verifyResult = & $signTool "verify" "/pa" "/v" "`"$ExecutablePath`""
    if ($LASTEXITCODE -eq 0) {
      Write-Host "Assinatura verificada com sucesso!" -ForegroundColor Green
    } else {
      Write-Host "Erro na verificacao da assinatura" -ForegroundColor Yellow
    }
  } else {
    Write-Error "Erro ao assinar executavel"
    Write-Host "Saida do SignTool:" -ForegroundColor Red
    Write-Host $result -ForegroundColor Red
    exit 1
  }
} catch {
  Write-Error "Erro durante assinatura: $($_.Exception.Message)"
  exit 1
}

# Informações finais
Write-Host ("`nInformacoes Finais:") -ForegroundColor Cyan
$fileInfo = Get-Item $ExecutablePath
Write-Host "   Arquivo: $($fileInfo.Name)" -ForegroundColor White
Write-Host "   Tamanho: $([math]::Round($fileInfo.Length / 1MB, 2)) MB" -ForegroundColor White
Write-Host "   Status: Assinado digitalmente" -ForegroundColor Green
$hash = Get-FileHash $ExecutablePath -Algorithm SHA256
Write-Host "   SHA256: $($hash.Hash)" -ForegroundColor White
# Salvar hash para verificacao
$hashFile = "$ExecutablePath.sha256"
$hash.Hash | Out-File $hashFile -Encoding UTF8
Write-Host "   Hash salvo em: $hashFile" -ForegroundColor Green
Write-Host ("`nProcesso concluido com sucesso!") -ForegroundColor Green
