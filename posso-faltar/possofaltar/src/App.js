import React, { useState, useEffect } from 'react';

function App() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/') // Altere a URL conforme necessário
      .then(response => response.json())
      .then(data => setUsuarios(data))
      .catch(error => console.error('Erro ao buscar usuários:', error));
  }, []);

  return (
    <div className='userlist'>
      <h1>Lista de Usuários</h1>
      
      <div>
        {usuarios.map(usuario => (
          <div key={usuario.id}>
            <strong>Nome:</strong> {usuario.nome} | <strong>Email:</strong> {usuario.email}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
