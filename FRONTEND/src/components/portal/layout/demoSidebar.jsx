"use client";
// import { SidebarInset } from "../ui/sidebar";

// import { Separator } from "../../components/ui/separator";
import { Separator } from "../../ui/separator";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "../../ui/breadcrumb";
// import Socials from "@/components/socials";
import {
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarTrigger,
} from "../../ui/sidebar";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "../../ui/tooltip";
import { SidebarInset } from "../../ui/sidebar";

import { useTheme } from "next-themes";
import {
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "../../ui/dropdown-menu";
import { ChevronsUpDown, SunMoon } from "lucide-react";

export function AppSidebarInset({ children }) {
  const { theme, setTheme } = useTheme();

  console.log(theme);

  return (
    <SidebarInset className="overflow-x-hidden ">
      <header className="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12 justify-between border-b dark:bg-[--sidebar-bg]  ">
        <div className="flex items-center gap-2 px-4 ">
          <Tooltip>
            <TooltipTrigger asChild>
              <SidebarTrigger id="trigger" className="-ml-1" />
            </TooltipTrigger>
            <TooltipContent side="bottom" align="start">
              Toggle Sidebar <kbd className="ml-2">⌘+b</kbd>
            </TooltipContent>
          </Tooltip>
          <Separator orientation="vertical" className="mr-2 h-4" />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem className="hidden md:block">
                <BreadcrumbLink href="/">Home</BreadcrumbLink>
              </BreadcrumbItem>
              <BreadcrumbSeparator className="hidden md:block" />
              <BreadcrumbItem>
                {/* <BreadcrumbPage className="block md:hidden">
                  Sidebar is only resizable on desktop
                </BreadcrumbPage> */}
                <BreadcrumbPage className="hidden md:block">
                  Alumni Portal
                </BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
        <div className="mr-2 sm:mr-4">
          {/* Theme switcher */}

          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <SidebarMenuButton
                id="variant"
                size="lg"
                className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground "
              >
                <div className="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground border-none outline-none">
                  <SunMoon className="size-4" />
                </div>
                {/* <div className="grid flex-1 text-left text-sm leading-tight">
                  <span className="truncate font-semibold">Select Theme</span>
                  <span className="truncate text-xs">sub text</span>
                </div> */}
                {/* <ChevronsUpDown className="ml-auto" /> */}
              </SidebarMenuButton>
            </DropdownMenuTrigger>
            <DropdownMenuContent
              className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
              align="end"
              side="top"
              sideOffset={4}
            >
              <DropdownMenuLabel className="text-xs text-muted-foreground">
                Themes
              </DropdownMenuLabel>
              {[
                {
                  name: "Light",
                  // logo: null,
                  key: "light",
                },
                {
                  name: "Dark",
                  // logo: null,
                  key: "dark",
                },
                {
                  name: "System",
                  // logo: null,
                  key: "system",
                },
              ].map((theme, index) => (
                <DropdownMenuItem
                  id={theme.name}
                  key={theme.name}
                  onClick={() => setTheme(theme.key)}
                  className="gap-2 p-2"
                >
                  {/* <div className="flex size-6 items-center justify-center rounded-sm border">
                    logo <team.logo className="size-4 shrink-0" />
                  </div> */}
                  {theme.name}
                  <DropdownMenuShortcut>⌘{index + 1}</DropdownMenuShortcut>
                </DropdownMenuItem>
              ))}
              <DropdownMenuSeparator />
              {/* <DropdownMenuItem className="gap-2 p-2">
              <div className="flex size-6 items-center justify-center rounded-md border bg-background">
                <Plus className="size-4" />
              </div>
              <div className="font-medium text-muted-foreground">Add team</div>
            </DropdownMenuItem> */}
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </header>

      <div className="sm:p-5 py-5 h-[93vh] overflow-y-auto bg-[--base-bg]  dark:bg-[--light-bg-dark]">
        {children}
      </div>
    </SidebarInset>
  );
}


import React from "react";
import Link from "next/link";
import { useSession, signOut } from "next-auth/react";
import { 
  GraduationCap, 
  Users, 
  Target, 
  MessageSquare,
  Home,
  User,
  Briefcase,
  Calendar,
  BookOpen,
  Info,
  Phone,
  Settings,
  Bell,
  LogOut,
  FileText,
  CircleUserRound,
  BadgeCheck,
  Building2,
  Camera,
  Shield
} from "lucide-react";

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
} from "../../ui/sidebar";
import { DropdownMenu, DropdownMenuGroup } from "@radix-ui/react-dropdown-menu";


// Navigation structure
const navigationGroups = [
  {
    title: "Main",
    items: [
      {
        title: "Dashboard",
        url: "/portal",
        icon: Home,
      },
      {
        title: "Eligibility",
        url: "/portal/eligibility",
        icon: FileText,
      },
      {
        title: "Rooms & Facilities",
        url: "/portal/rooms-facilities",
        icon: Building2,
      },
      {
        title: "Gallery",
        url: "/portal/gallery",
        icon: Camera,
      },
      {
        title: "TABH Administration",
        url: "/portal/administration",
        icon: Shield,
      },
      {
        title: "Events",
        url: "/portal/events",
        icon: Calendar,
      },
    ],
  },
  {
    title: "Resources",
    items: [
      {
        title: "About TABH",
        url: "/portal/about-alumni",
        icon: Info,
      },
      {
        title: "Contact",
        url: "/portal/contact",
        icon: Phone,
      },
    ],
  },
];

export function DemoSidebar() {
  const { data: session } = useSession();
  
  // Add admin items for superusers
  const getNavigationGroups = () => {
    const groups = [...navigationGroups];
    
    
    return groups;
  };

  return (
    <Sidebar>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton size="lg" asChild>
              <Link href="/portal">
                <div className="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                  <GraduationCap className="size-4" />
                </div>
                <div className="grid flex-1 text-left text-sm leading-tight">
                  <span className="truncate font-semibold">TABH</span>
                  <span className="truncate text-xs">Hostel Portal</span>
                </div>
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      
      <SidebarContent>
        {getNavigationGroups().map((group) => (
          <SidebarGroup key={group.title}>
            <SidebarGroupLabel>{group.title}</SidebarGroupLabel>
            <SidebarGroupContent>
              <SidebarMenu>
                {group.items.map((item) => (
                  <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton asChild>
                      <Link href={item.url}>
                        <item.icon className="w-4 h-4" />
                        <span>{item.title}</span>
                      </Link>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                ))}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        ))}
      </SidebarContent>

      <SidebarFooter>
        <SidebarMenu>
          <SidebarMenuItem>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <SidebarMenuButton
                  size="lg"
                  className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
                >
                  <CircleUserRound className="h-8 w-8" />
                  <div className="grid flex-1 text-left text-sm leading-tight">
                    <span className="truncate font-semibold">
                      {session?.user?.user_info?.first_name || "User"} {session?.user?.user_info?.last_name || ""}
                    </span>
                    <span className="truncate text-xs">
                      {session?.user?.user_info?.email || "user@example.com"}
                    </span>
                  </div>
                  <ChevronsUpDown className="ml-auto size-4" />
                </SidebarMenuButton>
              </DropdownMenuTrigger>
              <DropdownMenuContent
                className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
                side="bottom"
                align="end"
                sideOffset={4}
              >
                <DropdownMenuLabel className="p-0 font-normal">
                  <div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                    <CircleUserRound className="h-8 w-8" />
                    <div className="grid flex-1 text-left text-sm leading-tight">
                      <span className="truncate font-semibold">
                        {session?.user?.user_info?.first_name || "User"} {session?.user?.user_info?.last_name || ""}
                      </span>
                      <span className="truncate text-xs">
                        {session?.user?.user_info?.email || "user@example.com"}
                      </span>
                    </div>
                  </div>
                </DropdownMenuLabel>
                <DropdownMenuSeparator />
                <DropdownMenuGroup>
                  <DropdownMenuItem asChild>
                    <Link href="/portal/profile">
                      <BadgeCheck className="w-4 h-4" />
                      Account
                    </Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem asChild>
                    <Link href="/portal/settings">
                      <Settings className="w-4 h-4" />
                      Settings
                    </Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem asChild>
                    <Link href="/portal/notifications">
                      <Bell className="w-4 h-4" />
                      Notifications
                    </Link>
                  </DropdownMenuItem>
                </DropdownMenuGroup>
                <DropdownMenuSeparator />
                <DropdownMenuItem
                  className="cursor-pointer"
                  onClick={() => signOut()}
                >
                  <LogOut className="w-4 h-4" />
                  Log out
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
    </Sidebar>
  );
}