# 📋 Checklist de Desenvolvimento - Ordem do Dia

## 🎯 Antes de Começar

### Ambiente de Desenvolvimento
- [ ] Python 3.11+ instalado
- [ ] Git configurado com seu usuário
- [ ] VS Code com extensões Python instaladas
- [ ] Ambiente virtual criado (`.venv`)
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivos de exemplo na pasta `arquivos/`

### Configuração do Projeto
- [ ] `.gitignore` configurado
- [ ] `pytest.ini` configurado
- [ ] `requirements.txt` atualizado
- [ ] Hooks de git instalados (opcional)
- [ ] Editor configurado (formatação, linting)

## 🔧 Durante o Desenvolvimento

### Padrões de Código
- [ ] Seguir PEP 8 (usar `black` para formatação)
- [ ] Adicionar type hints em funções públicas
- [ ] Escrever docstrings para classes e métodos públicos
- [ ] Usar nomes descritivos para variáveis e funções
- [ ] Manter funções pequenas (máximo 50 linhas)

### Tratamento de Erros
- [ ] Usar `try/except` específicos (evitar `except Exception`)
- [ ] Logar erros com mensagens descritivas
- [ ] Validar inputs de usuário
- [ ] Verificar existência de arquivos antes de usar
- [ ] Retornar valores booleanos ou None em caso de erro

### Interface Gráfica (GUI)
- [ ] Seguir paleta de cores acessível
- [ ] Testar contraste (mínimo 4.5:1)
- [ ] Adicionar tooltips informativos
- [ ] Implementar estados visuais (hover, disabled)
- [ ] Usar threading para operações longas
- [ ] Atualizar barra de progresso durante processamento
- [ ] Exibir mensagens de feedback (toast notifications)

### Logs e Debugging
- [ ] Adicionar logs informativos com emojis
- [ ] Usar níveis de log apropriados (INFO, WARNING, ERROR)
- [ ] Testar com dados inválidos
- [ ] Verificar comportamento com arquivos corrompidos
- [ ] Validar memória durante processamento longo

## 🧪 Testes

### Testes Unitários
- [ ] Escrever testes para cada função nova
- [ ] Testar casos de sucesso e falha
- [ ] Usar mocks para dependências externas
- [ ] Manter cobertura mínima de 80%
- [ ] Executar `pytest` antes de cada commit

### Testes de Integração
- [ ] Testar fluxo completo de geração de OD
- [ ] Validar com arquivos PDF reais
- [ ] Testar com diferentes tamanhos de CSV
- [ ] Verificar output Excel gerado
- [ ] Testar cenários de erro (arquivos ausentes)

### Testes de Interface
- [ ] Testar inicialização da GUI
- [ ] Verificar responsividade dos botões
- [ ] Testar seleção de dias
- [ ] Validar exibição de toasts
- [ ] Verificar logs em tempo real

## 📦 Build e Distribuição

### Antes do Build
- [ ] Executar todos os testes (`pytest`)
- [ ] Verificar cobertura (`pytest --cov`)
- [ ] Executar linting (`black .` e `flake8`)
- [ ] Validar type hints (`mypy`)
- [ ] Testar GUI manualmente

### Processo de Build
- [ ] Executar `python build_exe.py`
- [ ] Verificar se executável é criado
- [ ] Testar executável standalone
- [ ] Validar estrutura de distribuição
- [ ] Verificar tamanho do arquivo final (~45-50MB)

### Validação do Executável
- [ ] Executável inicia sem erros
- [ ] Interface gráfica abre corretamente
- [ ] Verificação de arquivos funciona
- [ ] Geração de OD completa funciona
- [ ] Toast notifications aparecem
- [ ] Logs são exibidos corretamente

## 🚀 Antes do Commit

### Checklist Rápido
- [ ] Código formatado (`black .`)
- [ ] Sem erros de linting (`flake8`)
- [ ] Testes passando (`pytest`)
- [ ] Cobertura adequada (`pytest --cov`)
- [ ] Executável funciona (`python build_exe.py && test`)

### Mensagem de Commit
- [ ] Usar formato Conventional Commits
- [ ] Ser específico sobre as mudanças
- [ ] Incluir breaking changes se houver
- [ ] Referenciar issues relacionadas

Exemplos:
```
feat: adiciona sistema de toast notifications na GUI
fix: corrige erro de encoding em arquivos CSV  
docs: atualiza README com novas funcionalidades
test: adiciona testes para validação de PDF
```

## 📋 Antes do Pull Request

### Documentação
- [ ] README.md atualizado se necessário
- [ ] Docstrings adicionadas/atualizadas
- [ ] Comentários explicativos em código complexo
- [ ] CHANGELOG.md atualizado (se aplicável)

### Testes Finais
- [ ] Executar suite completa de testes
- [ ] Testar em ambiente limpo
- [ ] Validar executável em máquina diferente
- [ ] Screenshots da GUI (se mudanças visuais)

### Review Checklist
- [ ] Código auto-documentado
- [ ] Sem código comentado desnecessário
- [ ] Sem imports não utilizados
- [ ] Variáveis temporárias removidas
- [ ] Performance otimizada

## 🏷️ Antes do Release

### Versionamento
- [ ] Definir versão seguindo SemVer (MAJOR.MINOR.PATCH)
- [ ] Atualizar número da versão no código
- [ ] Criar tag no Git
- [ ] Atualizar CHANGELOG.md

### Distribuição
- [ ] Executável testado em múltiplas máquinas
- [ ] Documentação de usuário atualizada
- [ ] Pasta de distribuição completa
- [ ] ZIP de distribuição criado
- [ ] Assets uploadeados no GitHub Releases

### Comunicação
- [ ] Release notes escritas
- [ ] Stakeholders notificados
- [ ] Documentação deployada
- [ ] Equipe treinada (se necessário)

## 🔄 Manutenção Contínua

### Monitoramento
- [ ] Verificar feedback de usuários
- [ ] Monitorar issues no GitHub
- [ ] Acompanhar performance
- [ ] Validar compatibilidade com novas versões do Windows

### Atualizações
- [ ] Dependências atualizadas regularmente
- [ ] Testes executados após atualizações
- [ ] Documentação mantida atualizada
- [ ] Backup de versões estáveis

## 🆘 Solução de Problemas

### Debugging Comum
- [ ] Verificar logs de erro
- [ ] Testar com dados mínimos
- [ ] Isolar problema em função específica
- [ ] Usar debugger do VS Code
- [ ] Consultar documentação das bibliotecas

### Performance Issues
- [ ] Verificar uso de memória
- [ ] Otimizar loops demorados
- [ ] Usar profiling tools
- [ ] Implementar cache quando apropriado
- [ ] Dividir operações grandes em chunks

### GUI Issues
- [ ] Testar em diferentes resoluções
- [ ] Verificar threading adequado
- [ ] Validar estados de componentes
- [ ] Testar com diferentes themes do Windows
- [ ] Verificar acessibilidade

---

## ✅ Template de Checklist para PRs

Copie e cole este checklist em seus Pull Requests:

```markdown
## Checklist

### Desenvolvimento
- [ ] Código segue padrões do projeto
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Executável testado

### Testes
- [ ] Testes unitários passando
- [ ] Testes de integração passando  
- [ ] Cobertura mínima mantida (80%+)
- [ ] GUI testada manualmente

### Build
- [ ] Executável gera sem erros
- [ ] Funcionalidade testada no .exe
- [ ] Tamanho do arquivo aceitável
- [ ] Performance mantida/melhorada

### Review
- [ ] Código reviewed por ao menos 1 pessoa
- [ ] Breaking changes documentadas
- [ ] Versionamento considerado
- [ ] Deploy plan definido (se aplicável)
```
