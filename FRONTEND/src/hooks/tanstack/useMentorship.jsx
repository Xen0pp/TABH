"use client";

import axiosRequest from "../../lib/axiosRequest";
import { useMutation, useQueryClient, useQuery } from "@tanstack/react-query";
import { useSession } from "next-auth/react";

// Get all approved mentors
export const useGetMentors = ({ expertise = "", company = "" } = {}) => {
  const { data: session } = useSession();
  
  return useQuery({
    queryKey: ["mentors", expertise, company],
    queryFn: async () => {
      try {
        const params = new URLSearchParams();
        if (expertise) params.append("expertise", expertise);
        if (company) params.append("company", company);
        
        return await axiosRequest({
          url: `/mentorship/mentors/?${params.toString()}`,
          method: "GET",
          // headers: {
          //   Authorization: `Bearer ${session?.accessToken}`,
          // },
          timeout: 10000, // 10 second timeout
        });
      } catch (error) {
        console.error('Error fetching mentors:', error);
        // Return empty data structure instead of throwing
        return { data: [] };
      }
    },
    enabled: true,
    retry: 1,
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
  });
};

// Get mentor profile by ID
export const useGetMentorProfile = (mentorId) => {
  const { data: session } = useSession();
  
  return useQuery({
    queryKey: ["mentor", mentorId],
    queryFn: async () => {
      try {
        return await axiosRequest({
          url: `/mentorship/mentors/${mentorId}/`,
          method: "GET",
          // headers: {
          //   Authorization: `Bearer ${session?.accessToken}`,
          // },
          timeout: 10000,
        });
      } catch (error) {
        console.error('Error fetching mentor profile:', error);
        return { data: null };
      }
    },
    enabled: !!session?.accessToken && !!mentorId,
    retry: 1,
  });
};

// Apply as mentor
export const useApplyAsMentor = () => {
  const queryClient = useQueryClient();
  const { data: session } = useSession();

  return useMutation({
    mutationKey: ["applyAsMentor"],
    mutationFn: async (mentorData) =>
      await axiosRequest({
        url: `/mentorship/mentors/`,
        method: "POST",
        data: mentorData,
        // headers: {
        //   Authorization: `Bearer ${session?.accessToken}`,
        // },
        timeout: 15000,
      }),
    onSuccess: () => {
      queryClient.invalidateQueries(["mentors"]);
    },
  });
};

// Get user's mentorship requests (as mentee or mentor)
export const useGetMentorshipRequests = (type = "all") => {
  const { data: session } = useSession();
  
  return useQuery({
    queryKey: ["mentorshipRequests", type],
    queryFn: async () => {
      try {
        return await axiosRequest({
          url: `/mentorship/mentorship-requests/?type=${type}`,
          method: "GET",
          // headers: {
          //   Authorization: `Bearer ${session?.accessToken}`,
          // },
          timeout: 10000,
        });
      } catch (error) {
        console.error('Error fetching mentorship requests:', error);
        return { data: [] };
      }
    },
    enabled: !!session?.accessToken,
    retry: 1,
    staleTime: 2 * 60 * 1000, // 2 minutes
  });
};

// Create mentorship request
export const useCreateMentorshipRequest = () => {
  const queryClient = useQueryClient();
  const { data: session } = useSession();

  return useMutation({
    mutationKey: ["createMentorshipRequest"],
    mutationFn: async (requestData) =>
      await axiosRequest({
        url: `/mentorship/mentorship-requests/`,
        method: "POST",
        data: requestData,
        // headers: {
        //   Authorization: `Bearer ${session?.accessToken}`,
        // },
        timeout: 15000,
      }),
    onSuccess: () => {
      queryClient.invalidateQueries(["mentorshipRequests"]);
    },
  });
};

// Update mentorship request (accept/reject/update progress)
export const useUpdateMentorshipRequest = () => {
  const queryClient = useQueryClient();
  const { data: session } = useSession();

  return useMutation({
    mutationKey: ["updateMentorshipRequest"],
    mutationFn: async ({ requestId, updateData }) =>
      await axiosRequest({
        url: `/mentorship/mentorship-requests/${requestId}/`,
        method: "PUT",
        data: updateData,
        // headers: {
        //   Authorization: `Bearer ${session?.accessToken}`,
        // },
        timeout: 15000,
      }),
    onSuccess: () => {
      queryClient.invalidateQueries(["mentorshipRequests"]);
    },
  });
};
