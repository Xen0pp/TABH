'use client';

import { DemoSidebar } from "../../components/portal/layout/demoSidebar";
import { ThemeProvider } from "next-themes";
import { SessionProvider } from "next-auth/react";

export default function StartDemo() {
    return (
        <SessionProvider>
            <ThemeProvider attribute="class" defaultTheme="light" enableSystem>
                <div className="flex min-h-screen bg-background">
                    <DemoSidebar />
                        
                </div>
            </ThemeProvider>
        </SessionProvider>
    );
}
