import React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  Box,
  Flex,
  Spacer,
  Link,
  Button,
  Icon,
  HStack,
  Heading,
  Text,
} from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import useEventStore from "../../store/eventStore";

export const EventDetails = () => {
  const { eventID } = useParams();
  const navigate = useNavigate();

  const { fetchEventDetails, event, loading, error } = useEventStore();

  const formattedDate = (date) => {
    return new Date(date).toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  useEffect(() => {
    // Fetch event details from the backend using eventID
    const fetchEvent = async () => {
      try {
        fetchEventDetails(eventID);
      } catch (error) {
        console.error("Error fetching event details:", error);
      }
    };

    fetchEvent();
  }, [eventID]); // Run the effect when eventID changes

  const handleClick = () => {
    navigate(`/events/booking/${event.EventID}`);
  };

  return (
    <Flex w="100%" flexDirection={"column"}>
      {event ? (
        <>
          <Flex
            bgRepeat="no-repeat"
            bgSize="cover"
            bgPosition={"50% 0px"}
            bgImage={`url(${event.ImageUrl})`}
            textAlign="center"
            py={16}
            px={8}
            w="100%"
            flexDirection={"column"}
            color={"brand.secondary"}
            minHeight={"50vh"}
            justifyContent={"flex-end"}
            overflow="hidden" // Ensure no overflow if content exceeds bounds
            position="relative"
            _before={{
              content: '""',
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              bgGradient:
                "linear(to-r, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 100%)",
              zIndex: 1, // Overlay above the background image but below content
            }}
          ></Flex>

          {/* Event Title */}
          <Flex
            flexDirection={"column"}
            p={{ sm: "4", md: "8", lg: "10", xl: "10" }}
          >
            <Heading as="h1" fontSize="4xl" mb={4}>
              {event.Name}
            </Heading>

            {/* Event Description */}
            <Text fontSize="lg" mb={6} color="gray.600">
              {event.Description}
            </Text>

            <Flex direction={{ base: "column", md: "row" }} gap={8} mb={8}>
              {/* Venue Details */}
              <Box flex="1" p={6} bg="gray.50" borderRadius="md" boxShadow="md">
                <Heading as="h3" fontSize="2xl" mb={4}>
                  Venue Details
                </Heading>
                <Text fontSize="md" color="gray.700">
                  Madison Square Garden, New York City, NY
                </Text>
                <Text fontSize="md" color="gray.700">
                  4 Pennsylvania Plaza, New York, NY 10001
                </Text>
              </Box>

              {/* Event Date */}
              <Box flex="1" p={6} bg="gray.50" borderRadius="md" boxShadow="md">
                <Heading as="h3" fontSize="2xl" mb={4}>
                  Event Date & Time
                </Heading>
                <Text fontSize="md" color="gray.700">
                  {formattedDate(event.Date)}
                </Text>
              </Box>
            </Flex>

            {/* Book Tickets Button */}
            <Button
              colorScheme="brand.primary"
              bg="brand.primary"
              size="lg"
              w={{ base: "100%", md: "auto" }}
              px={12}
              py={6}
              onClick={handleClick}
            >
              Book Tickets
            </Button>
          </Flex>
        </>
      ) : (
        <p>Loading event details...</p>
      )}
    </Flex>
  );
};
