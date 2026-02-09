/**
 * Scripts gerais da aplicação Quina
 * Funções utilitárias e helpers
 */

// Formata valores monetários
function formatarValor(valor) {
    return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(valor);
}

// Formata data
function formatarData(data) {
    if (!data) return 'N/A';
    
    // Se já está no formato DD/MM/YYYY, retorna
    if (data.includes('/')) return data;
    
    // Tenta converter ISO para DD/MM/YYYY
    try {
        const [ano, mes, dia] = data.split('-');
        return `${dia}/${mes}/${ano}`;
    } catch {
        return data;
    }
}

// Valida número da Quina (1-80)
function validarNumero(numero) {
    const num = parseInt(numero);
    return !isNaN(num) && num >= 1 && num <= 80;
}

// Valida jogo completo
function validarJogo(numeros) {
    if (!Array.isArray(numeros)) return false;
    if (numeros.length < 5 || numeros.length > 15) return false;
    
    // Verifica duplicados
    const unicos = new Set(numeros);
    if (unicos.size !== numeros.length) return false;
    
    // Verifica range
    return numeros.every(validarNumero);
}

// Formata número com zero à esquerda
function pad(numero) {
    return String(numero).padStart(2, '0');
}

// Mostra notificação
function mostrarNotificacao(mensagem, tipo = 'info') {
    // Remove notificações anteriores
    const existentes = document.querySelectorAll('.notificacao');
    existentes.forEach(n => n.remove());
    
    const notificacao = document.createElement('div');
    notificacao.className = `notificacao notificacao-${tipo}`;
    notificacao.textContent = mensagem;
    
    document.body.appendChild(notificacao);
    
    // Remove após 3 segundos
    setTimeout(() => {
        notificacao.style.opacity = '0';
        setTimeout(() => notificacao.remove(), 300);
    }, 3000);
}

// Adiciona estilos para notificações
if (!document.getElementById('notification-styles')) {
    const style = document.createElement('style');
    style.id = 'notification-styles';
    style.textContent = `
        .notificacao {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 9999;
            transition: opacity 0.3s;
            font-weight: 600;
        }
        
        .notificacao-info {
            border-left: 4px solid #2196F3;
            color: #2196F3;
        }
        
        .notificacao-success {
            border-left: 4px solid #4CAF50;
            color: #4CAF50;
        }
        
        .notificacao-error {
            border-left: 4px solid #f44336;
            color: #f44336;
        }
        
        .notificacao-warning {
            border-left: 4px solid #ff9800;
            color: #ff9800;
        }
    `;
    document.head.appendChild(style);
}

// Scroll suave
function scrollSuave(elemento) {
    if (typeof elemento === 'string') {
        elemento = document.querySelector(elemento);
    }
    
    if (elemento) {
        elemento.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Debounce para otimizar eventos
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Exporta funções para uso global
window.MegaSena = {
    formatarValor,
    formatarData,
    validarNumero,
    validarJogo,
    pad,
    mostrarNotificacao,
    scrollSuave,
    debounce
};
