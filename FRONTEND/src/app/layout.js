import { Inter } from "next/font/google";
import "./globals.css";
import { getServerSession } from "next-auth/next";
import { authOptions } from "./api/auth/[...nextauth]/authOptions";
import CustomRootProvider from "../providers/CustomRootProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "VIPS-TC Alumni Portal",
  description: "Connect with VIPS Technical Campus alumni and build lasting professional networks",
};

// const myFont = localFont({
//   src: "./cambria-font.ttf",
//   display: "swap",
// });

export default async function RootLayout({ children }) {
  const session = await getServerSession(authOptions);

  return (
    <html suppressHydrationWarning lang="en">
      {/* <body className={myFont.className}> */}
      <body className={inter.className}>
        <CustomRootProvider session={session}>{children}</CustomRootProvider>
      </body>
    </html>
  );
}
