import Message from "./Message";
import { Button } from "@/components/ui/button";

function App() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950">
      <div className="space-y-4 text-center">
        <h1 className="text-4xl font-bold text-white">
          shadcn + Tailwind Working
        </h1>

        <Button>Test Button</Button>
      </div>
    </main>
  );
}

export default App;
