// Interatividade 1: Menu hamburguer responsivo
const btnMenu = document.getElementById('btn-menu');
const menu = document.getElementById('menu');

btnMenu.addEventListener('click', () => {
  menu.classList.toggle('ativo'); 
});

// Interatividade 2: Validação de formulário e feedback visual (manipulação DOM)
const formContato = document.getElementById('form-contato');
const mensagemFeedback = document.getElementById('mensagem-feedback');

formContato.addEventListener('submit', function(evento) {  
  evento.preventDefault(); 
  
  const nome = document.getElementById('nome').value;
  const email = document.getElementById('email').value;
  
  if(nome !== '' && email !== '') {
    mensagemFeedback.style.display = 'block';
    mensagemFeedback.style.color = '#4f46e5'; 
    mensagemFeedback.innerText = `Obrigado pelo contato ${nome}!\nRetornaremos no e-mail ${email} em breve.`;
    
    formContato.reset(); 
  } else {
    mensagemFeedback.style.display = 'block';
    mensagemFeedback.style.color = 'red';
    mensagemFeedback.innerText = 'Por favor, preencha todos os campos obrigatórios.';
  }
});