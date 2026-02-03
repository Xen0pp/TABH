"use client";

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
  ChevronsUpDown,
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
  SidebarMenuButton,
  SidebarMenuItem,
} from "../../../components/ui/sidebar";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../../../components/ui/dropdown-menu";

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
    ],
  },
  {
    title: "Brotherhood Network",
    items: [
      {
        title: "Profile",
        url: "/portal/profile",
        icon: User,
      },
      {
        title: "Alumni",
        url: "/portal/alumni-list",
        icon: Users,
      },
      {
        title: "Hostelers",
        url: "/portal/students",
        icon: GraduationCap,
      },
      {
        title: "Events",
        url: "/portal/events",
        icon: Calendar,
      },
      {
        title: "Jobs",
        url: "/portal/job-list",
        icon: Briefcase,
      },
    ],
  },
  {
    title: "Guidance & Mentorship",
    items: [
      {
        title: "Mentorship Hub",
        url: "/portal/mentorship",
        icon: Target,
      },
      {
        title: "Find Mentors",
        url: "/portal/mentorship/mentors",
        icon: Users,
      },
      {
        title: "Become a Mentor",
        url: "/portal/mentorship/apply-mentor",
        icon: MessageSquare,
      },
      {
        title: "My Mentorships",
        url: "/portal/mentorship/my-mentorships",
        icon: MessageSquare,
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

export function AppSidebar() {
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