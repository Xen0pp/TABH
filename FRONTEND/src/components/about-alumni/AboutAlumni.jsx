"use client";
import { motion, AnimatePresence } from "framer-motion";
import { useTheme } from "next-themes";
import Link from "next/link";
import Image from "next/image";
import {
  Users,
  Trophy,
  GraduationCap,
  Globe,
  Building,
  Briefcase,
  ArrowRight,
  Facebook,
  Twitter,
  Linkedin,
  Instagram,
  ChevronRight,
  Sparkles,
  Network,
  Award,
} from "lucide-react";

const AboutAlumni = () => {
  const { resolvedTheme } = useTheme();
  const isDark = resolvedTheme === "dark";

  return (
    <div
      className={`min-h-screen w-full p-4 md:p-8 rounded-xl ${
        isDark
          ? "bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900"
          : "bg-gradient-to-br from-vips-cream via-white to-vips-cream"
      }`}
    >
      <AnimatePresence>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="max-w-6xl mx-auto"
        >
          {/* Hero Section with animated banner */}
          <Card isDark={isDark} className="mb-8 overflow-hidden">
            <div
              className={`relative h-64 ${
                isDark
                  ? "bg-gradient-to-r from-violet-600 to-indigo-600"
                  : "bg-gradient-to-r from-sky-400 to-indigo-400"
              }`}
            >
              <motion.div
                className="absolute inset-0"
                initial={{ opacity: 0 }}
                animate={{
                  opacity: [0.2, 0.3, 0.2],
                  backgroundPosition: ["0% 0%", "100% 100%", "0% 0%"],
                }}
                transition={{
                  duration: 10,
                  repeat: Number.POSITIVE_INFINITY,
                  repeatType: "reverse",
                }}
                style={{
                  backgroundImage:
                    "url(\"data:image/svg+xml,%3Csvg display ='none' width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fillOpacity='0.1' fillRule='evenodd'/%3E%3C/svg%3E\")",
                }}
              >
                <div className="text-center relative z-10">
                  <motion.div
                    initial={{ y: -20, opacity: 0 }}
                    animate={{ y: 0, opacity: 1 }}
                    transition={{ delay: 0.2 }}
                  >
                    <div className="inline-block mb-4">
                      <div className="bg-white/20 backdrop-blur-md p-3 rounded-full">
                        <Network className="h-10 w-10 text-white" />
                      </div>
                    </div>
                    <h1 className="text-4xl md:text-5xl font-bold text-white mb-2">
                      Tauras Army Boys Hostel
                    </h1>
                    <p className="text-lg text-white/80 max-w-2xl mx-auto">
                      Forging bonds of honor and discipline, building a legacy of service, courage, and brotherhood
                    </p>
                  </motion.div>
                </div>
              </motion.div>
            </div>

            <div className="px-6 py-8">
              {/* Mission Statement */}
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.3 }}
                className="mb-8"
              >
                <InfoSection title="Our Mission" isDark={isDark}>
                  <p
                    className={
                      isDark
                        ? "text-gray-300 leading-relaxed"
                        : "text-gray-700 leading-relaxed"
                    }
                  >
                    The Tauras Army Boys Hostel (TABH) stands as a beacon of discipline, honor, and excellence. Our Brotherhood Network connects former residents who have been molded by the values of courage, integrity, and selfless service. We foster a lifelong bond among those who have walked these halls, instilling the spirit of camaraderie and national pride. Our network empowers former hostelers to carry forward the legacy of TABH—upholding the highest standards of character, leadership, and dedication to the nation in all their endeavors.

                  </p>
                </InfoSection>
              </motion.div>

              {/* Alumni Overview Grid */}
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.4 }}
                className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12"
              >
                <motion.div
                  whileHover={{ y: -5 }}
                  transition={{ type: "spring", stiffness: 300 }}
                >
                  <Card
                    className={
                      isDark
                        ? "bg-black/30 border-white/5 h-full"
                        : "bg-white/60 border-black/5 shadow-md h-full"
                    }
                    isDark={isDark}
                  >
                    <div className="p-6 flex flex-col h-full">
                      <div className="flex items-center gap-4 mb-4">
                        <div
                          className={`w-12 h-12 rounded-lg flex items-center justify-center ${
                            isDark
                              ? "bg-gradient-to-br from-purple-500/30 to-purple-500/10"
                              : "bg-gradient-to-br from-blue-400/30 to-blue-400/10"
                          }`}
                        >
                          <GraduationCap className="text-[--secondary-bg] h-6 w-6" />
                        </div>
                        <h3
                          className={`text-xl font-semibold ${
                            isDark ? "text-white" : "text-gray-800"
                          }`}
                        >
                          Academic Excellence
                        </h3>
                      </div>
                      <p className={isDark ? "text-gray-300" : "text-gray-700"}>
                      Our hostelers embody the finest traditions of discipline and excellence. Shaped by rigorous training in character, leadership, and moral values, they have gone on to serve the nation with distinction in the armed forces, civil services, and various professional fields. The foundation laid at TABH—built on honor, duty, and sacrifice—has produced individuals who stand tall as pillars of integrity and courage in society.</p>
                    </div>
                  </Card>
                </motion.div>

                <motion.div
                  whileHover={{ y: -5 }}
                  transition={{ type: "spring", stiffness: 300 }}
                >
                  <Card
                    className={
                      isDark
                        ? "bg-black/30 border-white/5 h-full"
                        : "bg-white/60 border-black/5 shadow-md h-full"
                    }
                    isDark={isDark}
                  >
                    <div className="p-6 flex flex-col h-full">
                      <div className="flex items-center gap-4 mb-4">
                        <div
                          className={`w-12 h-12 rounded-lg flex items-center justify-center ${
                            isDark
                              ? "bg-gradient-to-br from-purple-500/30 to-purple-500/10"
                              : "bg-gradient-to-br from-blue-400/30 to-blue-400/10"
                          }`}
                        >
                          <Briefcase className="text-[--secondary-bg] h-6 w-6" />
                        </div>
                        <h3
                          className={`text-xl font-semibold ${
                            isDark ? "text-white" : "text-gray-800"
                          }`}
                        >
                          Service to the Nation
                        </h3>
                      </div>
                      <p className={isDark ? "text-gray-300" : "text-gray-700"}>
                      TABH hostelers have distinguished themselves in service to the nation and society. Many have joined the Indian Armed Forces, serving with valor and dedication on the frontlines. Others have excelled in civil services, law enforcement, and leadership positions across various sectors. The values of discipline, teamwork, and unwavering commitment instilled at TABH continue to guide them as they contribute to nation-building and uphold the highest ideals of duty and honor.


                      </p>
                    </div>
                  </Card>
                </motion.div>
              </motion.div>

              {/* Key Stats Section */}
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.5 }}
                className="mb-12"
              >
                <h2
                  className={`text-2xl font-semibold mb-6 flex items-center gap-2 ${
                    isDark ? "text-white" : "text-gray-800"
                  }`}
                >
                  <span
                    className={`h-5 w-1 rounded-full ${
                      isDark
                        ? "bg-gradient-to-b from-purple-500 to-blue-500"
                        : "bg-gradient-to-b from-blue-400 to-indigo-500"
                    }`}
                  ></span>
                  Legacy of Excellence
                </h2>

                <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                  <StatCard
                    title="20+"
                    icon={<Users size={24} />}
                    description="Years of Building Character and Discipline"
                    isDark={isDark}
                  />
                  <StatCard
                    title="500+"
                    icon={<Trophy size={24} />}
                    description="Proud Hostelers Serving the Nation"
                    isDark={isDark}
                  />
                  <StatCard
                    title="100%"
                    icon={<Building size={24} />}
                    description="Commitment to Honor and Integrity"
                    isDark={isDark}
                  />
                  <StatCard
                    title="∞"
                    icon={<Globe size={24} />}
                    description="Brotherhood that Transcends Time"
                    isDark={isDark}
                  />
                </div>
              </motion.div>

              {/* Alumni Testimonials */}
              {/* <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.6 }}
                className="mb-12"
              >
                <h2
                  className={`text-2xl font-semibold mb-6 flex items-center gap-2 ${
                    isDark ? "text-white" : "text-gray-800"
                  }`}
                >
                  <span
                    className={`h-5 w-1 rounded-full ${
                      isDark
                        ? "bg-gradient-to-b from-purple-500 to-blue-500"
                        : "bg-gradient-to-b from-blue-400 to-indigo-500"
                    }`}
                  ></span>
                  Alumni Voices
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <Testimonial
                    name="Dr. Fahmida Rahman"
                    role="Senior Research Scientist, NASA"
                    message="My journey from UAP to NASA was built on the strong foundation I received during my undergraduate years. The rigorous curriculum and supportive faculty encouraged me to pursue my passion for aerospace engineering. Today, I'm proud to contribute to space exploration projects while mentoring current UAP students."
                    image="/placeholder.svg?height=80&width=80"
                    isDark={isDark}
                  />
                  <Testimonial
                    name="Tanvir Ahmed"
                    role="Co-founder & CTO, TechBangla"
                    message="UAP's entrepreneurship ecosystem gave me the confidence to launch my own tech startup. The alumni network has been invaluable for finding mentors, early clients, and even investors. Our company now employs over 50 people, including several UAP graduates who are bringing fresh ideas to our team."
                    image="/placeholder.svg?height=80&width=80"
                    isDark={isDark}
                  />
                </div>
              </motion.div> */}

              {/* Programs and Initiatives */}
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.7 }}
                className="mb-12"
              >
                <h2
                  className={`text-2xl font-semibold mb-6 flex items-center gap-2 ${
                    isDark ? "text-white" : "text-gray-800"
                  }`}
                >
                  <span
                    className={`h-5 w-1 rounded-full ${
                      isDark
                        ? "bg-gradient-to-b from-purple-500 to-blue-500"
                        : "bg-gradient-to-b from-blue-400 to-indigo-500"
                    }`}
                  ></span>
                  Brotherhood Programs
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <ProgramCard
                    title="Mentorship & Guidance"
                    description="Senior hostelers guide current residents in character building, career planning, and upholding the values of honor and discipline."
                    icon={<Sparkles size={20} />}
                    isDark={isDark}
                  />
                  <ProgramCard
                    title="Annual Reunion"
                    description="Brothers reunite to celebrate our shared legacy, honor achievements, and strengthen the bonds forged at TABH."
                    icon={<Users size={20} />}
                    isDark={isDark}
                  />
                  <ProgramCard
                    title="Welfare & Support"
                    description="Supporting fellow hostelers and their families, embodying the spirit of service and brotherhood beyond the hostel walls."
                    icon={<Award size={20} />}
                    isDark={isDark}
                  />
                </div>
              </motion.div>

              {/* Social Media and Connect */}
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.8 }}
                className="grid grid-cols-1 md:grid-cols-2 gap-8"
              >
                <div>
                  <h2
                    className={`text-2xl font-semibold mb-6 flex items-center gap-2 ${
                      isDark ? "text-white" : "text-gray-800"
                    }`}
                  >
                    <span
                      className={`h-5 w-1 rounded-full ${
                        isDark
                          ? "bg-gradient-to-b from-purple-500 to-blue-500"
                          : "bg-gradient-to-b from-blue-400 to-indigo-500"
                      }`}
                    ></span>
                    Stay Connected
                  </h2>

                  <div className="flex flex-wrap gap-4">
                    <SocialMediaButton
                      icon={<Facebook size={18} />}
                      label="Facebook"
                      link="https://www.facebook.com/UAP.Bangladesh"
                      isDark={isDark}
                    />
                    <SocialMediaButton
                      icon={<Twitter size={18} />}
                      label="Twitter"
                      link="https://twitter.com/UAP_BD"
                      isDark={isDark}
                    />
                    <SocialMediaButton
                      icon={<Linkedin size={18} />}
                      label="LinkedIn"
                      link="https://www.linkedin.com/school/uap-bd/"
                      isDark={isDark}
                    />
                    <SocialMediaButton
                      icon={<Instagram size={18} />}
                      label="Instagram"
                      link="https://www.instagram.com/uap.bd/"
                      isDark={isDark}
                    />
                  </div>
                </div>

                <div>
                  <h2
                    className={`text-2xl font-semibold mb-6 flex items-center gap-2 ${
                      isDark ? "text-white" : "text-gray-800"
                    }`}
                  >
                    <span
                      className={`h-5 w-1 rounded-full ${
                        isDark
                          ? "bg-gradient-to-b from-purple-500 to-blue-500"
                          : "bg-gradient-to-b from-blue-400 to-indigo-500"
                      }`}
                    ></span>
                    Get Involved
                  </h2>

                  <Link href="/portal/alumni-list">
                    <motion.button
                      className="relative overflow-hidden group text-sm font-medium bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-full h-12 flex gap-2 items-center justify-center px-6 w-full mb-4"
                      whileHover={{ scale: 1.02 }}
                      whileTap={{ scale: 0.98 }}
                    >
                      <motion.span className="absolute inset-0 bg-gradient-to-r from-purple-700 to-blue-700 opacity-0 group-hover:opacity-100 transition-opacity duration-200" />
                      <span className="relative flex items-center gap-2">
                        <span>Explore Brotherhood Profiles</span>
                        <ArrowRight
                          size={16}
                          className="group-hover:translate-x-1 transition-transform duration-200"
                        />
                      </span>
                    </motion.button>
                  </Link>

                  <Link href="/portal/events">
                    <motion.button
                      className={`relative overflow-hidden group text-sm font-medium w-full rounded-full h-12 flex gap-2 items-center justify-center px-6 ${
                        isDark
                          ? "bg-black/30 border border-white/10 text-white hover:bg-white/10"
                          : "bg-white/50 border border-black/10 text-gray-800 hover:bg-black/5"
                      }`}
                      whileHover={{ scale: 1.02 }}
                      whileTap={{ scale: 0.98 }}
                    >
                      <span className="flex items-center gap-2">
                        <span>View Upcoming Brotherhood Events</span>
                        <ChevronRight size={16} />
                      </span>
                    </motion.button>
                  </Link>
                </div>
              </motion.div>
            </div>
          </Card>
        </motion.div>
      </AnimatePresence>
    </div>
  );
};

// Card Component
const Card = ({ children, className = "", isDark }) => (
  <div
    className={`rounded-xl overflow-hidden ${
      isDark
        ? "backdrop-blur-md bg-black/20 border border-white/10"
        : "backdrop-blur-md bg-white/70 border border-black/5 shadow-xl"
    } ${className}`}
  >
    {children}
  </div>
);

// Info Section Component
const InfoSection = ({ title, children, isDark }) => (
  <div className="space-y-3 mb-6">
    <h3
      className={`text-xl font-semibold flex items-center gap-2 ${
        isDark ? "text-white/90" : "text-gray-800"
      }`}
    >
      <span
        className={`h-5 w-1 rounded-full ${
          isDark
            ? "bg-gradient-to-b from-purple-500 to-blue-500"
            : "bg-gradient-to-b from-blue-400 to-indigo-500"
        }`}
      ></span>
      {title}
    </h3>
    <div className="pl-3">{children}</div>
  </div>
);

// Stat Card Component
const StatCard = ({ title, icon, description, isDark }) => (
  <motion.div
    whileHover={{ y: -5, scale: 1.02 }}
    transition={{ type: "spring", stiffness: 300 }}
    className={`p-6 rounded-xl ${
      isDark
        ? "bg-black/30 border border-white/10"
        : "bg-white/60 border border-black/5 shadow-md"
    }`}
  >
    <div
      className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 ${
        isDark
          ? "bg-gradient-to-br from-purple-500/30 to-purple-500/10"
          : "bg-gradient-to-br from-blue-400/30 to-blue-400/10"
      }`}
    >
      <div className="text-[--secondary-bg]">{icon}</div>
    </div>
    <h3
      className={`text-2xl font-bold mb-1 ${
        isDark ? "text-white" : "text-gray-800"
      }`}
    >
      {title}
    </h3>
    <p className={isDark ? "text-gray-400 text-sm" : "text-gray-600 text-sm"}>
      {description}
    </p>
  </motion.div>
);

// Testimonial Component
const Testimonial = ({ name, role, message, image, isDark }) => (
  <motion.div
    whileHover={{ y: -5 }}
    transition={{ type: "spring", stiffness: 300 }}
    className={`p-6 rounded-xl ${
      isDark
        ? "bg-black/30 border border-white/10"
        : "bg-white/60 border border-black/5 shadow-md"
    }`}
  >
    <div className="flex items-start gap-4">
      <div className="relative w-16 h-16 rounded-full overflow-hidden flex-shrink-0">
        <Image
          src={image || "/placeholder.svg"}
          alt={name}
          fill
          className="object-cover"
        />
      </div>
      <div>
        <p
          className={`italic mb-4 ${
            isDark ? "text-gray-300" : "text-gray-700"
          }`}
        >
          "{message}"
        </p>
        <h4
          className={`font-semibold ${isDark ? "text-white" : "text-gray-800"}`}
        >
          {name}
        </h4>
        <p
          className={isDark ? "text-gray-400 text-sm" : "text-gray-600 text-sm"}
        >
          {role}
        </p>
      </div>
    </div>
  </motion.div>
);

// Program Card Component
const ProgramCard = ({ title, description, icon, isDark }) => (
  <motion.div
    whileHover={{ y: -5 }}
    transition={{ type: "spring", stiffness: 300 }}
    className={`p-5 rounded-xl ${
      isDark
        ? "bg-black/30 border border-white/10"
        : "bg-white/60 border border-black/5 shadow-md"
    }`}
  >
    <div className="flex items-center gap-3 mb-3">
      <div
        className={`w-8 h-8 rounded-lg flex items-center justify-center ${
          isDark
            ? "bg-gradient-to-br from-purple-500/30 to-purple-500/10"
            : "bg-gradient-to-br from-blue-400/30 to-blue-400/10"
        }`}
      >
        <div className="text-[--secondary-bg]">{icon}</div>
      </div>
      <h3
        className={`font-semibold ${isDark ? "text-white" : "text-gray-800"}`}
      >
        {title}
      </h3>
    </div>
    <p className={isDark ? "text-gray-400 text-sm" : "text-gray-600 text-sm"}>
      {description}
    </p>
  </motion.div>
);

// Social Media Button Component
const SocialMediaButton = ({ icon, label, link, isDark }) => (
  <Link href={link} target="_blank" rel="noopener noreferrer">
    <motion.button
      className={`flex items-center gap-2 px-4 py-2 rounded-full ${
        isDark
          ? "bg-black/30 border border-white/10 text-white hover:bg-white/10"
          : "bg-white/50 border border-black/10 text-gray-800 hover:bg-black/5"
      }`}
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
    >
      <div className="text-[--secondary-bg]">{icon}</div>
      <span>{label}</span>
    </motion.button>
  </Link>
);

export default AboutAlumni;
