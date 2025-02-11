import { Box, Image, Text, Link, Icon, VStack, Flex } from "@chakra-ui/react";
import { FaChevronRight } from "react-icons/fa";

import { useState } from "react";

export const EventCard = (props) => {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <Link
      w={{ sm: "100%", md: "45%", lg: "45%", xl: "45%" }}
      minWidth={"300px"}
      borderRadius={"5"}
      href={`/events/${props.eventID}`}
    >
      <VStack
        textAlign={"start"}
        alignItems={"center"}
        justifyItems={"center"}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        borderRadius={"5"}
      >
        <Flex
          position="relative"
          w="100%"
          h="350px"
          minHeight={"300px"}
          bgRepeat="no-repeat"
          bgSize="cover"
          bgPosition={"50% 0px"}
          bgImage={`url(${props.image})`}
          alignItems={"center"}
          justifyContent={"flex-end"}
          borderRadius={"5"}
          _hover={{
            _before: {
              content: '""',
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              bg: "rgba(2, 77, 223, 0.15)", // Set overlay color and opacity
              zIndex: 1,
            },
            "> *": {
              // Targets child elements to bring them above the overlay
              zIndex: 2,
            },
            boxShadow: "lg",
          }}
        >
          {isHovered && (
            <Flex
              bgColor={"#024ddf"}
              height={"100%"}
              alignItems={"center"}
              p="1"
              borderRadius={"0 5px 5px 0"}
            >
              <Icon
                as={FaChevronRight}
                boxSize={6}
                color="white"
                transition="opacity 0.6s ease"
              />
            </Flex>
          )}
        </Flex>
        <Flex w="100%" textAlign={"start"} flexDirection={"column"} p={"2"}>
          <Text>{props.description}</Text>
          <Text fontSize="lg" fontWeight="bold" color="brand.primary">
            {props.title}
          </Text>
        </Flex>
      </VStack>
    </Link>
  );
};
