import { useState, useEffect } from 'react'
import { NeoCard, NeoButton, initNeural } from '@jikey8911/jeikei-ui'

function App() {
  const [status, setStatus] = useState('STANDBY')

  useEffect(() => {
    const canvas = document.getElementById("neural") as HTMLCanvasElement;
    if (canvas) initNeural(canvas);
  }, []);

  return (
    <div className="min-h-screen bg-neo-bg text-white relative overflow-hidden flex flex-col items-center justify-center p-8">
      {/* Neural Background */}
      <canvas id="neural" className="fixed inset-0 z-0 opacity-40 pointer-events-none" />

      <div className="z-10 w-full max-w-4xl flex flex-col gap-8">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-glow-cyan text-neo-cyan tracking-widest">AUTOMCLAW SYSTEM</h1>
          <p className="text-neo-cyan/70 mt-2 tracking-widest">STRATEGIC AUTONOMOUS UNITS</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <NeoCard 
            title="CORE ENGINE" 
            value="ONLINE" 
            status="SYNCED" 
            variant="cyan" 
          />
          <NeoCard 
            title="PROCESS OPTIMIZATION" 
            value={status} 
            status="AWAITING COMMAND" 
            variant="magenta" 
          />
        </div>

        <div className="flex justify-center gap-4 mt-8">
          <NeoButton variant="cyan" onClick={() => setStatus('ANALYZING...')}>
            INITIATE ANALYSIS
          </NeoButton>
          <NeoButton variant="danger" onClick={() => setStatus('HALTED')}>
            EMERGENCY STOP
          </NeoButton>
        </div>
      </div>
    </div>
  )
}

export default App
