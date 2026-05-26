import httpx
import asyncio
from news_framework import BaseNewsAgent

class FutebolDesportoAgent(BaseNewsAgent):
    """
    Agente especializado em recolher e processar notícias de futebol,
    focando em competições como Champions League e Copa do Mundo.
    """
    
    def __init__(self):
        super().__init__(
            agent_name="Geraldo_Sense (Champions League e Copa do Mundo)",
            topic="Champions League e Copa do Mundo"
        )
    
    async def collect_data(self):
        """
        Simula a recolha de dados de notícias de futebol.
        Em produção, isto conectaria a APIs de notícias desportivas.
        """
        # Dados de exemplo sobre notícias da Champions League e Copa do Mundo
        return {
            "title": "Champions League e Copa do Mundo: Análise dos grandes momentos",
            "content": "Análise detalhada dos últimos jogos da UEFA Champions League e da preparação para a Copa do Mundo. Destaques das melhores exibições, golos decisivos e as histórias que estão a marcar o futebol internacional.",
            "url": "https://www.uefa.com/uefachampionsleague/news/",
            "source": "UEFA/FIFA",
            "category": "Futebol Internacional"
        }
    
    async def process_with_ai(self, data):
        """
        Processa os dados recolhidos (simula processamento com IA).
        Em produção, integraria Hugging Face ou outro modelo de IA.
        """
        return {
            "summary": f"Resumo: {data.get('content', '')[:120]}... Veja mais em {data.get('url', 'N/A')}",
            "processed": True,
            "category": data.get("category", "Futebol Internacional"),
            "sentiment": "positivo"
        }
    
    async def run(self):
        """
        Método principal que orquestra a recolha, processamento e envio
        de notícias de futebol para o Hub Central.
        Implementa retry logic com exponential backoff para garantir entrega.
        """
        try:
            print("[INFO] 🚀 Iniciando Agente de Futebol Internacional: Champions League e Copa do Mundo...")
            
            # 1. Recolher dados
            raw_data = await self.collect_data()
            print(f"[INFO] 📰 Notícia recolhida: {raw_data['title']}")
            
            # 2. Processar com IA
            processed_data = await self.process_with_ai(raw_data)
            print(f"[INFO] ⚙️ Dados processados com sucesso")
            
            # 3. Preparar payload para envio
            payload = {
                "agent_name": self.agent_name,
                "topic": self.topic,
                "title": raw_data.get("title", "Notícia Desporto"),
                "summary": processed_data.get("summary", ""),
                "url": raw_data.get("url", "https://www.uefa.com/uefachampionsleague/news/"),
                "confidence": 1.0,
            }
            
            # 4. Configurar headers
            headers = {
                "Content-Type": "application/json",
                "x-token": "epf2026_secret"
            }
            
            # 5. URL do Hub Central (servidor remoto)
            url_hub = "https://news2pi.onrender.com/publish"
            
            # 6. Configurar timeouts (conexão, leitura)
            timeout = httpx.Timeout(30.0)
            
            # 7. Retry logic com 3 tentativas
            async with httpx.AsyncClient(timeout=timeout) as client:
                last_err = None
                
                for attempt in range(1, 4):
                    try:
                        print(f"[ATTEMPT] 📡 Tentativa {attempt}/3 de conexão ao Hub...")
                        
                        response = await client.post(
                            url_hub,
                            json=payload,
                            headers=headers
                        )
                        
                        print(f"[SUCCESS] ✅ Status: {response.status_code}")
                        print(f"[SUCCESS] 📊 Resposta: {response.text}")
                        
                        if response.status_code in [200, 201]:
                            print(f"[SUCCESS] 🎉 Notícia publicada com sucesso no Hub Central!")
                        
                        return response.status_code
                        
                    except (httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ConnectError) as e:
                        last_err = e
                        print(f"[RETRY] ⚠️ Tentativa {attempt}/3 falhou: {type(e).__name__}: {e}")
                        
                        if attempt < 3:
                            wait_time = 1.5 * attempt
                            print(f"[RETRY] ⏳ Aguardando {wait_time}s antes da próxima tentativa...")
                            await asyncio.sleep(wait_time)
                
                # Se chegamos aqui, todas as tentativas falharam
                print(f"[ERROR] ❌ Falha ao conectar ao Hub após 3 tentativas.")
                if last_err:
                    print(f"[ERROR] Último erro: {last_err}")
                return None
                
        except Exception as e:
            print(f"[ERROR] ❌ Erro no agente: {str(e)}")
            return None

# Para testes locais
if __name__ == "__main__":
    async def main() -> None:
        agent = FutebolDesportoAgent()
        await agent.run()
    
    asyncio.run(main())
