import React from "react";
import {
  Box,
  Flex,
  Text,
  Link,
  VStack,
  HStack,
  Icon,
  Image,
} from "@chakra-ui/react";
import { FaFacebookF, FaTwitter, FaYoutube, FaInstagram } from "react-icons/fa";

const Footer = () => {
  return (
    <Flex
      bg="gray.900"
      color="gray.400"
      py={10}
      px={{ base: 4, md: 8 }}
      direction={"column"}
      w={"100%"}
    >
      <Flex
        direction={{ base: "column", md: "row" }}
        justify="space-between"
        mb={8}
      >
        {/* Left Section - Logo and Social Media */}
        <VStack align="start" spacing={4}>
          <Text fontSize="lg" color="white" fontWeight="bold">
            ticketmaster
          </Text>
          <HStack spacing={4}>
            <Link href="#" isExternal>
              <Icon as={FaFacebookF} boxSize={5} />
            </Link>
            <Link href="#" isExternal>
              <Icon as={FaTwitter} boxSize={5} />
            </Link>
            <Link href="#" isExternal>
              <Icon as={FaYoutube} boxSize={5} />
            </Link>
            <Link href="#" isExternal>
              <Icon as={FaInstagram} boxSize={5} />
            </Link>
          </HStack>

          {/* App Download Links */}
          <HStack spacing={4}>
            <Image
              src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg"
              alt="Download on the App Store"
              height="40px"
            />
            <Image
              src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg"
              alt="Get it on Google Play"
              height="40px"
            />
          </HStack>
        </VStack>

        {/* Right Section - Footer Links */}
        <Flex
          direction={{ base: "column", md: "row" }}
          mt={{ base: 8, md: 0 }}
          spacing={8}
        >
          {/* Helpful Links */}
          <VStack align="start" spacing={2} mr={{ base: 0, md: 10 }}>
            <Text fontWeight="bold" color="white">
              Helpful Links
            </Text>
            <Link href="#">Help/FAQ</Link>
            <Link href="#">Sell</Link>
            <Link href="#">My Account</Link>
            <Link href="#">Contact Us</Link>
            <Link href="#">Gift Cards</Link>
          </VStack>

          {/* Our Network */}
          <VStack align="start" spacing={2} mr={{ base: 0, md: 10 }}>
            <Text fontWeight="bold" color="white">
              Our Network
            </Text>
            <Link href="#">Live Nation</Link>
            <Link href="#">House of Blues</Link>
            <Link href="#">Front Gate Tickets</Link>
            <Link href="#">TicketWeb</Link>
          </VStack>

          {/* About Us */}
          <VStack align="start" spacing={2} mr={{ base: 0, md: 10 }}>
            <Text fontWeight="bold" color="white">
              About Us
            </Text>
            <Link href="#">Ticketmaster Blog</Link>
            <Link href="#">Privacy Policy</Link>
            <Link href="#">Ad Choices</Link>
            <Link href="#">Careers</Link>
          </VStack>

          {/* Friends & Partners */}
          <VStack align="start" spacing={2}>
            <Text fontWeight="bold" color="white">
              Friends & Partners
            </Text>
            <Link href="#">PayPal</Link>
            <Link href="#">Allianz</Link>
            <Link href="#">AWS</Link>
          </VStack>
        </Flex>
      </Flex>
    </Flex>
  );
};

export default Footer;
